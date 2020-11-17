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

#### READING DATASET ####
indianFood = pd.read_csv("indian_food.csv")
food = pd.read_csv("Food_Preference.csv")

#### DISPLAYING DATA ####
st.title('Mon app en python')
st.header('Food preferences')
st.subheader('Dataset')
st.write(food.head(2)) #or st.table
st.subheader('Colonnes')
st.write(food.columns)
st.subheader('Type des colonnes')
st.write(food.dtypes)
st.subheader('Shape')
st.write(food.shape)
st.subheader('Info')
st.write(food.info())
#
st.header('Indian food')
st.subheader('Dataset')
st.write(indianFood.head(2)) #or st.table
st.subheader('Colonnes')
st.write(indianFood.columns)
st.subheader('Type des colonnes')
st.write(indianFood.dtypes)
st.subheader('Shape')
st.write(indianFood.shape)
st.subheader('Info')
st.write(food.info())

