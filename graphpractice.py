import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
data = pd.read_csv("titanic.csv")
data2 = pd.read_csv("iris.csv")
"""
count = data["Sex"].value_counts()
print(count)
mp.bar(count.index,count.values)
mp.show()

#how many passengers in each class

pclass_count = data["Pclass"].value_counts()
groups = ["Group 1","Group 2", "Group 3"]
time = pclass_count
mp.title("Passengers per group")
mp.pie(time,labels=pclass_count,autopct="%1.1f%%",colors=["Blue","Red","Green"],startangle=0,shadow=True)
mp.show()

#Create a histogram of passengers' ages.
list = []
ages = data["Age"]
mp.title("Ages")
intervals = [10,20,30,40,50,60,70,80,90,100]
mp.hist(ages.values,intervals)
mp.show()


#Create a bar chart showing the average fare for each passenger class
pclass_count = data["Pclass"]
result = data.groupby("Pclass")["Fare"].mean()
print(result)
mp.title("Average fare per class")
mp.xlabel("Class")
mp.ylabel("Fare")
mp.bar(result.index,result.values)
mp.show()

#Create a bar chart showing the survival rate by gender
result = data.groupby("Sex")["Survived"].mean()

print(result)

mp.title("Survival Rate by Gender")
mp.xlabel("Gender")
mp.ylabel("Survival Rate")
mp.bar(result.index, result.values)
mp.show()

#Create a scatter plot of Age vs Fare, using different colors for survivors and non-survivors.
survived = data[data["Survived"] == 1]
not_survived = data[data["Survived"] == 0]

mp.scatter(survived["Age"], survived["Fare"], label="Survived")
mp.scatter(not_survived["Age"], not_survived["Fare"], label="Did not survive")

mp.title("Age vs Fare")
mp.xlabel("Age")
mp.ylabel("Fare")
mp.legend()
mp.show()

#plot mean width of all categories bar graph
meanvalue = data2.groupby("species")["petal_width"].mean()

print(meanvalue)

mp.xlabel("Species")
mp.ylabel("Mean width")
mp.bar(meanvalue.index,meanvalue.values)
mp.show()
"""

#histogram showing the distribution of petal widths
values = data2["petal_width"]
intervals = [0,0.5,1,1.5,2]
mp.hist(values,intervals)
mp.show()
