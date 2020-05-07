# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 18:23:08 2020

@author: samed
"""

import pandas as pd 

veri=pd.read_excel('Adana-Çatalan-Günlük.xlsx')

# PM10 ortalaması alma işlemi


# PM10 ortalama

Pm10ortalama=veri["PM10 ( µg/m³ )"].mean()

# PM10 Gösterimi

import matplotlib.pyplot as plt

saatler = ['Ortalama']
degerler = [Pm10ortalama]

f=plt.figure(figsize=(12,6))
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.suptitle('Çatalan PM10 ( µg/m³ ) Ortalama Verisi')
plt.show()

