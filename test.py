import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Prostate Cancer Risk Prediction Chart', page_icon='🔬', layout='wide')

st.title('Prostate Cancer Risk Prediction Chart')

DATA_URL = ('pcra.csv')

@st.cache
def get_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data
  
df = get_data()

data_load_state = st.text('Loading data...')
data = get_data(10000)
data_load_state.text("Viewing Patient Data")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)




