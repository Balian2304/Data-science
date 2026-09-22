import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
data = pd.read_csv("titanic.csv")
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
"""

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
#Create a scatter plot of Age vs Fare, using different colors for survivors and non-survivors.
#Create a box plot showing Fare distribution by Pclass and Survival status
