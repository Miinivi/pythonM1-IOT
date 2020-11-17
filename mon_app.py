#### FIRST IMPORTS ####
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from pathlib import Path
sns.set()

#### SKLEARN ####
#!pip install -U scikit-learn
import sklearn 
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#### DATASET ####
food = pd.read_csv("Food_Preference.csv")
foodName = 'Food preferences'
indianFood = pd.read_csv("indian_food.csv")
indianFoodName = 'Indian food'
# We put the names in variables because we'll use it more than once.

#### TITLE ####
st.title('My python web app')

#### SELECT BOX ####
option = st.selectbox('Please, select a dataset',(foodName, indianFoodName))
st.write('You selected:', option)

#### USER INPUT ####
user_input = st.text_input("How many lines do you want to check in the dataset?", 5)

#### DISPLAYING DATA ####
def displayData(dataName, df, nbDatasetHead):
    st.header(dataName)
    st.subheader('Dataset')
    st.write(df.head(int(nbDatasetHead))) #or st.table
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.subheader('Columns')
        st.write(df.columns)
    with col2:
        st.subheader('Columns types')
        st.write(df.dtypes)
    with col3:
        st.subheader('Describe')
        st.write(df.describe())
    st.subheader('Shape')
    st.write(df.shape)
    st.subheader('Info')
    st.write(df.info())

if option == foodName:
    displayData(foodName, food, user_input)
else:
    displayData(indianFoodName, indianFood, user_input)


