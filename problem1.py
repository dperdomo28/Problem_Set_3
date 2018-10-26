#!/usr/bin/env python3

#Problem 1) Write a script that opens the file, uses a for loop to read through the file line by line and calculates the highest water level and the date and time that was observed.

#first we will read in the file

data_lines= open("CO-OPS__8729108__wl.csv", "r")

#for loop reading through each line 
highest_water_level= 0    #this must be a global variable; we define it as zero and it will later be changed as we read through the lines in file

for line in data_lines:
    try:  
       current_water_level= float(line.split(',')[1])  #water level is second column in file; we are extracting this column in each line to check water level and storing it as "current water level"
    except: continue

    if current_water_level > highest_water_level:
        highest_water_level= current_water_level  #if current water level was higher than our previous highest w.l., it will replace it as the new highest value
        highest_level_full_line= line             # we will store the line containing our present highest water level value, as this line contains date and time observed
    else:                                         #if our current water level was not higher than our stored highest value, continue on to check the next line
        continue
#here our for loop will have finished and if we print our stored values of highest_water_level, it should hold the true value. the variable highest_level_full_line will contain the line with this value, which is helpful because this line will hold the date and time info we want to look at. we simply have to extract the column with this information, as we will do:

print("highest water level:", highest_level_full_line.split(',')[1])       #printing highest water level from second column in line; using a useful print comment to identify it
print("date and time:", highest_level_full_line.split(',')[0])		   #printing date and time for corresponding max value; also using useful print comment to tell us what output means
