import pandas as pd
import plotly as pl
import matplotlib.pyplot as mp
import plotly.graph_objects as go
data = pd.read_csv("WHO-COVID-19-global-data.csv")

selectedcountry = input("Name a country: ")
data_country = data[data["Country"]==selectedcountry]
print(data_country)
cumulativecases = data_country["Cumulative_cases"]
figure = go.Figure(
    data=[
        go.Scatter(name="Cumulative Cases",x=data_country["DateReported"],y=data_country["Cumulative_cases"])
    ]
)
figure.write_html("figure.html",auto_open=True)

cumulativedeaths = data_country["Cumulative_deaths"]
figure2 = go.Figure(
    data=[
            go.Scatter(name = "Cumulative deaths",x=data_country["DateReported"],y=data_country["Cumulative_deaths"]),
            go.Scatter(name = "Cumulative cases",x=data_country["DateReported"],y=data_country["Cumulative_cases"]),
            go.Scatter(name= "Daily new cases",x=data_country["DateReported"],y=data_country["New_cases"],fill="tozeroy"),
            go.Scatter(name= "Daily new deaths",x=data_country["DateReported"],y=data_country["New_deaths"],fill="tozeroy")
    ]
)
figure2.write_html("figure2.html",auto_open=True)


figure3 = mp.figure()
mp.subplot(221)
mp.scatter(x=data_country["DateReported"],y=data_country["Cumulative_deaths"])
mp.subplot(222)
mp.scatter(x=data_country["DateReported"],y=data_country["Cumulative_cases"])
mp.subplot(223)
mp.scatter(x=data_country["DateReported"],y=data_country["New_cases"])
mp.subplot(224)
mp.scatter(x=data_country["DateReported"],y=data_country["New_deaths"])
mp.show()
