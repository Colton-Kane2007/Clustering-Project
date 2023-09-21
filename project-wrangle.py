import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from env import user, host, password
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
import newwrangle as w
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE, SelectKBest, f_regression
from sklearn.linear_model import LassoLars
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import TweedieRegressor
from scipy import stats
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def wrangle_wine():
    if os.path.isfile('wine.csv'):
        white = pd.read_csv('white.csv')
        red = pd.read_csv('red.csv')
    else:
        #creates new csv if one does not already exist
        print('Download the .csv from https://data.world/food/wine-quality')
    white.columns = white.columns.str.replace(' ', '_')
    white.columns = white.columns.str.lower()
    red.columns = red.columns.str.replace(' ', '_')
    red.columns = red.columns.str.lower()
    red['is_red'] = 1
    data = [white, red]
    df = pd.concat(data)
    red['is_red'] = 1
    # Rename columns
    df = df.rename(columns={
    'free_sulfur_dioxide': 'free_so2',
    'total_sulfur_dioxide': 'total_so2'
    })
    df.is_red = df.is_red.fillna(0)
    return df
