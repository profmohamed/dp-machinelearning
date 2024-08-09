import streamlit as st
import pandas as pd

st.title(' 🤖 Machine Learning App ')
st.info('this app builds  a machine learning model ')

with st.expander('Data'):
  st.write ('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

  st.write('**x**')
  x = df.drop('species', axis= 1)
  x
  
  st.write('**y**')
  y = df.species
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x ='bill_lenth_mm', y='body_mass_g', color= 'species')
