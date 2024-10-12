import os
import pandas as pd
from sklearn.model_selection import train_test_split

caminho_database_toda = 'src/database/NVDA.csv'
caminho_database_treino = 'src/database/NVDA_treino.csv'
caminho_database_teste = 'src/database/NVDA_teste.csv'

df = pd.read_csv(caminho_database_toda, sep=',')

carac = df[['Date', 'Open', 'High', 'Low', 'Volume', 'Adj Close']]
resp = df[['Close']]


X_treino, x_teste, y_treino, y_teste = train_test_split(carac, resp, test_size=0.2, random_state=43)
df_treino = pd.concat([X_treino, y_treino], axis=1)
df_teste = pd.concat([x_teste, y_teste], axis=1)

df_treino.to_csv(caminho_database_treino, index=False)
df_teste.to_csv(caminho_database_teste, index=False)

