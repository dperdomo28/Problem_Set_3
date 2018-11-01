#!/usr/bin/env python3

import pandas as pd#Dani: you have to import the module you want to use

# Question1
#Dani: in your for loop you typed 'lind' instead of line and it wasnt running, fixed it in this copy

pb3= pd.read_csv("file.pb3.csv") #Dani
#pb3 = open("file.pb3.csv") #original line

for line in pb3.readlines():
	WaterLevel = line.split(",")[1]
	print(WaterLevel) #Dani: I dont think you should print this; it would reduce the amount of output if you didnt
WaterLavel_list = []
WaterLavel_list.append(WaterLevel)
#Dani: you have to actually print the max
print(max(WaterLavel_list))
#Dani: your max value is 2.###; it should be 6.something. THere seems to be an error in the code. From looking at what is being printed 'Water Level', it appears the max value being returned is the last value in the list. I suggest looking into how to do this. Check out my code for another approach using for loops; dont forget you also have to give the date adn time where the max value is observed! i would suggest printing the line where it is found when you find the correct max value
#Dani: good thing is that the logic of your code is easy to follow; it seems it just didnt do what we expected


# Question2
pb3 = pandas.read_csv('file.pb3.csv')
print(pb3.max()) #Dani: remember you have to always use print function. Good job!! this works great and is very concise !! very easy to read/understand too


# Question3
#pb3_water = pb3.loc[:1] #Dani: code gives error here; says there is no attribute iloc. try running it using regular .loc
#DAni: i realized an error is that yuou are not reading the file into a pandas dataframe, you are simply opening it. try using pandas.read_csv('file')
pb3_water_1= pb3.loc[pb3[' Water Level'].idxmax()]
pb3_water= pb3_water_1.iloc[:2]
pb3_diff = pb3_water.diff()
#print(pb3_diff) Dani: the code wasnt working so in included a print statement here to check if this function is working properly and it gives me back an error. I suggest starting from the beginning and use test print satements aling the way to make sure you know what each section is doing
print(pb3_diff.max())

# Question4
pb3['Date Time'].str.split(' ', 1, expand = True)  #I use this code to separate ‘Date’ and ‘Time’
pb3_new = pd.concat([pb3['Date Time'].str.split(' ', 1, expand = True),pb3[[' Water Level']]], axis = 1, ignore_index = True)
x = pb3_new[[1]]
y = pb3_new[[2]]
import matplotlib.pyplot as plt
fig = plt.figure()
plt.plot(x[1],y[2])
fig.savefig('my_figure.png')

#great job! this is clear and easy to understand the logic. good job on including a useful comment
