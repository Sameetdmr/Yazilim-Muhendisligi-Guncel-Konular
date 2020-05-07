# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:51:51 2020

@author: samed
"""

import pandas as pd

veri=pd.read_excel('ValilikYeniVeri-8-18-00.xlsx')

Iliski=veri.corr()



import seaborn as sns
Iliski=veri.corr()
sns.heatmap(Iliski, 
            xticklabels=Iliski.columns.values,
            yticklabels=Iliski.columns.values)