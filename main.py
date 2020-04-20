#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[38]:


import pandas as pd
import numpy as np


# In[39]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[40]:


df = pd.DataFrame(black_friday)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[41]:


def q1():
    return df.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[42]:


def q2():
    # Acessa, compara e conta os registros que atendem os parametros informados.
    return int(((df["Gender"]=="F") & (df["Age"]=="26-35")).sum())
q2()


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[43]:


def q3():
    # Remover os registros com o campo ID repetido.
    return df["User_ID"].nunique()
q3()


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[44]:


def q4():
    # Informa o tipo e o número de colunas com determinado tipo
    return len(df.dtypes.value_counts())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[45]:


def q5():
    porcent = df["Product_Category_3"].isna().sum() / df.shape[0]
    return float(porcent)
q5()


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[46]:


def q6():
    return int(df.isnull().sum().max())


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[47]:


def q7():
    # Deve dar o valor mais frequente.
    return int(df['Product_Category_3'].mode())
q7()

    


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[48]:


def q8():
    v_max = df['Purchase'].max()
    v_min = df['Purchase'].min()
    result = (df['Purchase'] - v_min)/(v_max - v_min)
    return float(result.mean())
q8()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[49]:


def q9():
    purchase = df['Purchase']
    padronization = (purchase - purchase.mean())/(purchase.std())
    return int(padronization.between(-1,1).sum())
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[50]:


def q10():
    compare = df['Product_Category_2'].isnull() == df['Product_Category_3'].isnull()
    return (True in compare) 
q10()


# In[ ]:




