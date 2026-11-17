import pandas as pd
data = pd.read_csv("WHO-COVID-19-global-data.csv")

data["DateReported"] = pd.to_datetime(data["DateReported"])
data.info()
print(data[(data["DateReported"].dt.month==1) & (data["DateReported"].dt.day==5)]["New_deaths"].sum())

#find data for January 2026 New cases and new deaths
#for Afghanistan how many deaths in March 2026
