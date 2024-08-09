import streamlit as st
import pandas as pd

st.title(' 🤖 Machine Learning App ')
st.info('this app builds  a machine learning model ')

with st.expander('Data'):
  st.write ('**Raw data**')
  df = pd.read_scv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df
