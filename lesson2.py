import numpy as np
import pandas as pd
data = pd.read_csv("titanic.csv")
print(type(data))
"""
print(data.info())
print(data.head())
print(data.tail())
print(data.shape)
print(data.dtypes)
print(data)
print(data["Name"])
print(data[["Name","Age"]])
print(data.describe())
"""
#filtering out rows
print(data[data["Age"]>50])
print(data[(data["Sex"]=="female")&(data["Age"]>30)][["Name","Age"]])
print(data[(data["Survived"]==1)|(data["Pclass"]==1)])
print(data[(data["Survived"]==1)].count())
print(data["Survived"].value_counts())
print(data["Pclass"].value_counts())
print(data[(data["Pclass"]==1)&(data["Sex"]=="male")]["Fare"].mean())
print(data[(data["Pclass"]==1)&(data["Sex"]=="female")]["Fare"].mean())
print(data[(data["Pclass"]==2)&(data["Sex"]=="male")]["Fare"].mean())
print(data[(data["Pclass"]==2)&(data["Sex"]=="female")]["Fare"].mean())
print(data[(data["Pclass"]==3)&(data["Sex"]=="male")]["Fare"].mean())
print(data[(data["Pclass"]==3)&(data["Sex"]=="female")]["Fare"].mean())

newdata = pd.DataFrame({
    "Name":["Balian","Ibrahim","Daan"],
    "Age":[16,42,16],
    "Sex":["Male","Male","Male"]
})

print(newdata.info())
print(newdata.head())
print(newdata.tail())
print(newdata.shape)
print(newdata.dtypes)
