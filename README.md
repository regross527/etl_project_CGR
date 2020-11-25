# etl_project_CGR

GOAL/INTENT
The goal of the project was to compile specific baseball statistics unique to two different stat-focused websites to have the ability to show them beside one another for individual baseball players. Data was pulled from baseball-reference.com (BBREF) and fangraphs.com (FG), and specifically we sought to pull WAR (Wins Above Replacement), which each site calculates differently, and its related components. As a starting point, we began with the 2019 season and pulled individual player statistics for all hitters with a certain number of plate appearances. The eventual goal was to pull both player lists into separate tables within a MongoDB database for simplified comparison.

EXTRACT SUMMARY
Both BBREF and FG allow for simple filtering within their websites to display the relevant data, and both allow for easy CSV downloads after filtering. We chose to manually download these CSVs rather than scrape the data, for ease and sake of time. Neither website has an API. In the case of BBREF, multiple CSV files were needed as only 250 lines could be downloaded at a time. Upon seeing the how the data was displayed, we determined the best way to compare players across sites was to align their names so that they were identical in both tables.
	- files extracted in 00_input: bbref1.csv, bbref2.csv, bbref3.csv, FanGraphs Leaderboards 2019 hitters.csv

TRANSFORM SUMMARY
Upon seeing the how the data was displayed, we determined the best way to compare players across sites was to align their names so that they were identical in both tables. Due to prior knowledge of the subject matter, we knew that no names would be repeated. 

We had to take a few steps to ensure all the data lined up across both datasets:
1) Excel was used to quickly combine all BBREF CSVs into a single CSV file to be used for the rest of the transformations.
	- file in 00_input: bbrefFULL.csv
2) Python module unidecode was used to replace all accented letters with their simplified English equivalents.
	- files in 01_extract_bbref: bbref_cleanup.py, bbref_noaccents.csv
3) An Excel macro then removed all spaces, commas, periods, and hyphens from player names for both datasets.
	- CSV files had to be changed to .xlsx files and back for this step in the process.
	- files in 01_extract_bbref: bbref_noaccents.xlsx
	- files in 02_transform_bbref: remove_spaces_vba.bas, bbrefdataFINAL.csv
	- files in 02_transform_fangraphs: remove_spaces_FG_vba.bas, fangraphsFINAL.csv
4) As a final test, an outer join using null values showed a handful of names that still did not match (such as "Matthew Joyce" being "Matt Joyce" in the other dataset). These were manually changed in order to maintain congruency.
	- files in 02_transform_fangraphs: pandas_check_players.py

LOAD SUMMARY
Data was loaded into a MongoDB database as two separate tables -- one for the BBREF data and one for FG. Queries using "Player" as a primary key can compare and contrast statistics across the two different sites.
	- files in 02_transform_fangraphs: pandas_check_players.py

NEXT STEPS
Our first desired query would be to compare FanGraphs' WAR against Baseball-Reference's WAR directly in a simplified table to see if there are outliers or interesting trends. This was the main goal that drove the project from the get-go.

We would also be able to pull more years' worth of data, or even full careers of players with the same methodology. Finding more websites that focus on baseball statistics would open interesting avenues to explore in the future.