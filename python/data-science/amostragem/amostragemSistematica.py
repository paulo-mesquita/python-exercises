# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np 
from math import ceil


# %%
populacao = 150
amostra = 15
k = ceil(populacao / amostra)
# ceil faz o arredondamento para cima

r = np.random.randint(low = 1, high = k + 1, size = 1)
# faz o sorteio entre 1 a k + 1 ou seja de 1 a 10

acumulador = r[0]
sorteados = []

for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k


# %%
base = pd.read_csv('/home/haboryn/Programacao/PYTHON/vscode/RecursosdoCurso/Dados/iris.csv')
base_final = base.loc[sorteados]


# %%


