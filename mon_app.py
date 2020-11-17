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
indianFood = pd.read_csv("indian_food")
#### RESOLVING ERROR ####
#### CONCERNED DATASET #### 
# https://www.kaggle.com/northon/globalterrorismdatabase-compact

#### READING DATASET ####
food = pd.read_csv("Food_Preference.csv")
#### CONCERNED DATASET #### 
# https://www.kaggle.com/abcsds/pokemon/activity

#### DISPLAYING DATA ####
@st.cache
def load_data():
   data_path = Path() / 'Food_Preference.csv'
   data = pd.read_csv(data_path)
   return data

#pokemon_df = load_data()
st.write(food.head(5))