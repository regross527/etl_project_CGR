#!/usr/bin/env python
# coding: utf-8

get_ipython().system('git status')

# Import Module
import pandas as pd

# Import Fangraphs csv file.
file_to_load = "../FanGraphs_Leaderboards_2019_hitters-no_spaces.csv"
fangraphs_file = pd.read_csv(file_to_load)
fangraphs_df = pd.DataFrame(fangraphs_file)
fangraphs_df = fangraphs_df.rename(columns={'Name':'Player'})
fangraphs_df = fangraphs_df.set_index('Player')
fangraphs_df

# Import Baseball Reference csv file.  Also change the names of the players 
# whose names are different.
file_to_load = "../01_extract_bbref/bbref_noaccents.csv"
bref_file = pd.read_csv(file_to_load)
bref_df = pd.DataFrame(bref_file)
bref_df['Player'] = bref_df['Player'].replace(
    {'GioUrshela': 'GiovannyUrshela',
     'DeeStrangeGordon': 'DeeGordon',
    'AlbertAlmora':'AlbertAlmoraJr',
    'StevieWilkerson':'SteveWilkerson',
    'RichieMartin':'RichieMartinJr',
    'PhilErvin':'PhillipErvin',
    'MatthewJoyce':'MattJoyce',
    'YuChang':'YuChengChang',
    'CedricMullins':'CedricMullinsII'})
bref_df = bref_df.set_index('Player')
bref_df.head(30)

# Check to make sure all players match
bref_df.merge(fangraphs_df, 'outer', indicator=True, on='Player').query('_merge != "both"')

#create csv files of the final data
bref_df.to_csv('../02_transform_bbref/bbrefdataFINAL.csv')
fangraphs_df.to_csv('fangraphsFINAL.csv')




