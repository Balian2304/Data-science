import pandas as pd
data = pd.read_csv("covid_data.csv")
print(data.columns)
print(data.info())
data = data[["Province_State","Country_Region","Confirmed","Recovered","Active","Deaths"]]
print(data[data["Country_Region"]=="Australia"])
deaths_list = data[data["Country_Region"]=="Australia"]
print(deaths_list.sort_values(by="Deaths",ascending=False).head(1))
print(data.groupby("Country_Region")["Deaths"].sum().nlargest(10))

#print(data.sort_values(by="Deaths",ascending=False).head(10))
#use some practice questions
#top 10 states of US with highest deaths
#state with highest death count per country
