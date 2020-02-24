# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
import numpy as np

base1 = pd.read_csv('/home/haboryn/Programacao/PYTHON/vscode/RecursosdoCurso/Dados/iris.csv')
base1


# %%
np.random.seed(2345) # Faz com que gere os mesmos dados estatisticos sempre
amostra = np.random.choice(a = [0,1], size = 150, replace = True, p = [0.5,0.5])
# Neste exemplo se utiliza uma amostr com dois elementos [0,1] onde a reposição dos elementos
# Esta ativa com o comando: replace = True
# Assim a amostra aleatoria dos elementos pode chegar ao tamanho desejado que no caso é size = 150
# p = [0.5,0.5] - significa que a probabilidade de sorteio de cada elemento é de 50%
amostra


# %%
len(amostra) # informa quantos elementos possui


# %%
len(amostra[amostra==1]) # informa quantas vezes determinado elemento foi registrado


# %%
len(amostra[amostra==0]) # informa quantas vezes determinado elemento foi registrado


# %%


