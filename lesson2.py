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


print(data[data["Age"]<18])

print(data[(data["Sex"]=="male")&(data["Age"]>20)][["Name","Age"]])
print(data[(data["Survived"]==0)&(data["Age"]<30)][["Name","Age"]])
print(data[(data["Pclass"]==3)&(data["Age"]<30)][["Name","Age"]])
print(data.loc[data["Age"]>18,"Name"])
print(data.iloc[1:100:5,2:8:2])
data["discount"] = data["Fare"] * 0.1
print(data["discount"])
data.iloc[1:4:1,2] = "John"
print(data["Name"])
data.to_csv("Lesson2file.csv")
data_rename = data.rename(columns={"Fare":"Price","Sex":"Gender"})
data_rename.info()
print(data["Age"].mean())
print(data[["Fare","Age"]].mean())
print(data.agg({"Age":["sum","mean","median"],"Fare":["min","max","mean"]}))
print(data["Sex"].value_counts())
#groupby
print(data.groupby("Survived")["Fare"].count())
print(data.groupby("Survived")["Fare"].mean())
print(data.groupby("Sex")["Fare"].max())


