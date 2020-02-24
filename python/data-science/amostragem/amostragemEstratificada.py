# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from sklearn.model_selection import train_test_split


# %%
iris = pd.read_csv('/home/haboryn/Programacao/PYTHON/vscode/RecursosdoCurso/Dados/iris.csv')


# %%
iris['class'].value_counts()


# %%
x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:,4], test_size = 0.5, stratify = iris.iloc[:,4])


# %%
y.value_counts()


# %%
infert = pd.read_csv('/home/haboryn/Programacao/PYTHON/vscode/RecursosdoCurso/Dados/infert.csv')


# %%
infert['education'].value_counts()


# %%
x1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6, stratify = infert.iloc[:, 1])
# stratify indica o campo o qual queremos manuzear
# .iloc - todas as linhas
# o traco _, serve para que nao carregue a outra parte da base de dados e traga apenas a amostra 
y1.value_counts()


# %%


