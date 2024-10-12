import os
import pandas as pd
from sklearn.model_selection import train_test_split
from PATHS import CAMINHO_TESTE, CAMINHO_TREINO, CAMINHO_NVDA


df = pd.read_csv(CAMINHO_NVDA, sep=',')

carac = df[['Date', 'Open', 'High', 'Low', 'Volume', 'Adj Close']]
resp = df[['Close']]


X_treino, x_teste, y_treino, y_teste = train_test_split(carac, resp, test_size=0.2, random_state=43)
df_treino = pd.concat([X_treino, y_treino], axis=1)
df_teste = pd.concat([x_teste, y_teste], axis=1)

df_treino.to_csv(CAMINHO_TREINO, index=False)
df_teste.to_csv(CAMINHO_TESTE, index=False)

