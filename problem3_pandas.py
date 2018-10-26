#!/usr/bin/env python3

import pandas as pd

# 3) Write a script  that calculates the fastest rise in water level per 6-minute period between measurements and reports the data and time that was observed and the change in water level during that period. You can use line by line or dataframe for this.

wl_f = pd.read_csv("CO-OPS__8729108__wl.csv")  #reading in file into pandas dataframe

#We are using the very useful series.shift method to create a column called "difference" which will store the difference between n+1 row and nth row.
wl_f['Difference'] = wl_f[' Water Level'] - wl_f[' Water Level'].shift(+1)

#printing the comment highest rise, along with max value of difference column; we will round this value to 4 sig figs, if this is not done there are like 9 sig figs- unnecessary
print ('Highest Rise',wl_f.Difference.max().round(4))

#Here we will look for the corresponding before and after date&time and water level readings for the highest rise

Line_Number = wl_f.Difference.idxmax() #gives line number of highest rise from difference column
#the nth-1 row of the diff. column will correspond with nth values of water level column (the before rise value). we are accessing this line and then converting to a float and rounding because the output without this gives " water level #######" with many decimal places. 
print('Water_Level_Before_Rise',round(float(wl_f.ix[Line_Number-1,[1]]),3))

#line number in diff. column will correspond with date and time after the rise; so we can just look at this line number for the date and time column in wl_f
print ('Date_Time_After_Rise',wl_f.ix[Line_Number,'Date Time'])

#because of math, the line number of difference column will correspond with the nth+1 line; so we can just look at our first dataframe and the line from diff. in the water level column
print ('Water_Level_After_Rise',wl_f.ix[Line_Number,' Water Level'])

