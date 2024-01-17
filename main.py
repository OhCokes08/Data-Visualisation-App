import streamlit as st
import plotly.express as px
import pandas as pd



st.title("Countries Happiness Factors")
xaxis = st.selectbox("Select a metric for the x axis", ("GDP", "Happiness", "Generosity"))
yaxis = st.selectbox("Select a metric for the y axis", ("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

match xaxis:
    case "Happiness":
        xarray = df["happiness"]
    case "GDP":
        xarray = df["gdp"]
    case "Generosity":
        xarray = df["generosity"]
match yaxis:
    case "Happiness":
        yarray = df["happiness"]
    case "GDP":
        yarray = df["gdp"]
    case "Generosity":
        yarray = df["generosity"]

st.subheader(f"{xaxis} and {yaxis}")



figure = px.scatter(df, x=xarray, y=yarray, labels={"x":xaxis, "y":yaxis})
st.plotly_chart(figure)
