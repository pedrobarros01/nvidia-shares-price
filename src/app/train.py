import pandas as pd
import tensorflow as tf
import numpy as np
from src.utils.utils import transform_colum_date_datasset
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from PATHS import CAMINHO_TREINO


df_train = pd.read_csv(CAMINHO_TREINO, sep=',')
df_train = transform_colum_date_datasset(df_train)

caracs = df_train[['Timer_day', 'Open', 'High', 'Low', 'Volume', 'Adj Close']]
resp = df_train[['Close']]

