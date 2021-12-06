import streamlit as st
import  pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="Nanostics", page_icon="🤖")

df = pd.read_csv("Patient_Data.csv")

st.title("Prostate Cancer Risk Detection")

select = st.sidebar.selectbox('PATIENT NAME',['Tony Starck','Peter Parker','Steve Rogers', 'Bruce Banner', 'Bucky Burnes'], index=0)

#get the state selected in the selectbox
select_status = st.sidebar.radio("View Patient details by: ", (
    'Age',
    'Age of diagnosis', 
    'Year of first diagnosis', 
    'Year of first diagnosis', 
    'Year of third diagnosis',
    'PSA at diagnosis (ng/ml)',
    'Gleason scode ',
    'Clinical stage'))

