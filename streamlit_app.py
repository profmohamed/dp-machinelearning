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
  st.scatter_chart(data=df, x ='bill_length_mm', y='body_mass_g', color= 'species')

# Data preparations
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Bisco','Dream', 'Torgersen'))
  bill_length_mm = st.slider('Bill lenght (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_lenght_mm = st.slider('Flipper lenght (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0,)
  gender = st.selectbox('Gender',('male', 'female'))

  # create a data frame for the input feasures
  data  = {'island': island,
          'bill_length_mm': bill_length_mm,
          'bill_depth_mm': bill_depth_mm,
          'flipper_lenght_mm' : flipper_lenght_mm,
          'body_mass_g' : body_mass_g,
          'sex' : gender}
  input_df = pd.DataFrame(data, index=[0])
  input_penguins = pd.concat([input_df, x], axis=0)
with st.expander('Input features'):
  st.write('**Input penguin**')
  input_df
  st.write('**Combined penguins data **')
  input_penguins
encode = ['island', 'sex']
df_penguins = pd.get_dummies(input_penguins, prefix=encode)




















