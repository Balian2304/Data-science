import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly 
import plotly.express as pe
import plotly.graph_objects as go
data = pd.read_csv("covid_data.csv")
data = data[["Province_State","Country_Region","Confirmed","Recovered","Active","Deaths"]]
data["Province_State"].fillna(value=' ',inplace=True)
#bubbleplot
#top 10 most affected country
#mostaffected = pd.DataFrame(data.groupby("Country_Region")["Confirmed"].sum().nlargest(10).sort_values(ascending=False))
#scattergraph = pe.scatter(mostaffected,x=mostaffected.index,y="Confirmed",size="Confirmed",size_max=100,color=mostaffected.index)
#scattergraph.write_html("covid_data.html",auto_open = True)
"""
mostdeaths = pd.DataFrame(data.groupby("Country_Region")["Deaths"].sum().nlargest(10).sort_values(ascending=False))
bargraph = pe.bar(mostdeaths,x=mostdeaths.index,y="Deaths",height=600,color="Deaths",color_continuous_scale=pe.colors.sequential.Bluyl_r)
bargraph.write_html("covid_data.html",auto_open=True)
mostrecovered = pd.DataFrame(data.groupby("Country_Region")["Recovered"].sum().nlargest(10).sort_values(ascending=False))
bargraph = pe.bar(mostrecovered,x=mostrecovered.index,y="Recovered",height=600,color="Recovered",color_continuous_scale=pe.colors.sequential.Bluyl_r)
bargraph.write_html("covid_data.html",auto_open=True)
"""
top5highestdeaths_us = pd.DataFrame(data[data["Country_Region"] == "US"].groupby("Province_State")["Deaths"].sum().nlargest(5).sort_values(ascending=False))
bargraph = pe.bar(top5highestdeaths_us,x=top5highestdeaths_us.index,y="Deaths")
bargraph.write_html("covid_data.html",auto_open=True)

