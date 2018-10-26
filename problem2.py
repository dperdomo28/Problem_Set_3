#!/usr/bin/env python3

import pandas as pd

# 2) Write a script (or Jupyter Notebook code block) that reads the file into a Pandas dataframe and calculates the highest water level and the date and time that was observed.
#our wl_f file is our pandas database file

wl_f= pd.read_csv("CO-OPS__8729108__wl.csv")   #reading in file into pandas dataframe; returns columns 1: date and time, column2: water level, etc.; but these are of our interest

#printing maximum of column [1] - water level; if found max, print the whole row, which contains date and time
max_row= wl_f.loc[wl_f[' Water Level'].idxmax()]

#print(wl_f.loc[wl_f[' Water Level'].idxmax()])   #test print statement

#the above line returns the max water level info but changes it to the headers being now in column 1 but in different rows; row 1 and 2 are date and time and water level respectively. SO, we will just pull out the first 2 rows of this "max row" dataframe

print(max_row.iloc[0:2])


