import csv 
import pandas as pd 
import plotly.graph_objects as go

df=pd.read_csv("data.csv")

print(df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Scatter(
    x=df.groupby("level")["attempt"].mean(),
    y=['Level1','level2','level3','level4'],
    orientation ='h'))

fig.show()