# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:36:59 2020

@author: samed
"""


import pandas as pd
import numpy as np
import seaborn as sns


df=pd.read_excel('Catalan-8-18-00.xlsx')

df.isnull().sum() ## Boş değer gösterimi

df.dtypes

dffs = df.select_dtypes(include=['float64'])

dffs.head()

dfft = df.select_dtypes(include=['datetime64[ns]'])

dfft.head()


dffs.describe().T

from fancyimpute import KNN

var_date = list(dfft)
var_names = list(dffs)
knn_imp = KNN(k=5).fit_transform(dffs)
knn_imp[0:10]
dff = pd.DataFrame(knn_imp)


dff.head()

dff.columns = var_names



dff.head()

date_var_concat = pd.concat([dfft, dff], axis=1, sort=False)

date_var_concat.head()



date_var_concat.isnull().sum()

veri = date_var_concat

veri.head()

veri.describe(include = 'all')

veri.nunique()

veri.isnull().sum()

veri.to_excel('EksikVeri.xlsx',index=False)










