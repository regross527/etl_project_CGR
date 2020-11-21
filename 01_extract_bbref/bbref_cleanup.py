import unidecode
import pandas as pd

# use compiled csv file to create pandas df for bbref data
bbrefdata = "../00_input/bbrefFULL.csv"
bbref_df = pd.read_csv(bbrefdata)
bbref_df.head()

# make Player column into a list
namelist = []

for name in bbref_df["Player"]:
    namelist.append(name)
    
# change all accented names into normalized English spellings
normalizednamelist = []

for item in namelist:
    normalizednamelist.append(unidecode.unidecode(item))
    
normalizednamelist

# split on \\ delimiter to clean column
finalname = []

for normal in normalizednamelist:
    splitname = normal.split('\\')
    finalname.append(splitname[0])
    
finalname

# put cleaned name list into dataframe
finalnameseries = pd.Series(finalname)
bbref_df["Player"] = finalnameseries
bbref_df = bbref_df.drop(columns="Rk")

bbref_df.head()

#send file to Excel file for next step in cleaning
bbref_df.to_excel("bbref_noaccents.xlsx")