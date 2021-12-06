import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame(px.data.gapminder())
clist = df['country'].unique()

country = st.sidebar.selectbox("Patient Name:",clist)

st.header("Prostate Cancer Risk Assessment")

fig = px.line(df[df['country'] == country], 
    x = "year", y = "gdpPercap", title = country)
st.plotly_chart(fig)