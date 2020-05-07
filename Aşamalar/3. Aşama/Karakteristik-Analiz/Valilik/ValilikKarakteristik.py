# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:48:37 2020

@author: samed
"""


import pandas as pd


veri=pd.read_excel('ValilikYeniVeri-8-18-00.xlsx')






# Veri seçim işlemi yapıldı

Saat8=veri[1:182:3]
Saat18=veri[0:182:3]
Saat00=veri[2:182:3]





#-----------------------------------------------------------------------------#

# Verilerin ortalamasını alma işlemi

# PM10 ortalama

Saat8ortalamaPm10=Saat8["PM10 ( µg/m³ )"].mean()

# SO2 ortalama

Saat8ortalamaSo2=Saat8["SO2 ( µg/m³ )"].mean()

# NO2 ortalama

Saat8ortalamaNo2=Saat8["NO2 ( µg/m³ )"].mean()

# O3 ortalama

Saat8ortalamaO3=Saat8["O3 ( µg/m³ )"].mean()

# CO ortalama

Saat8ortalamaCo=Saat8["CO ( µg/m³ )"].mean()


#-----------------------------------------------------------------------------#

# PM10 ortalama

Saat18ortalamaPm10=Saat18["PM10 ( µg/m³ )"].mean()

# SO2 ortalama

Saat18ortalamaSo2=Saat18["SO2 ( µg/m³ )"].mean()

# NO2 ortalama

Saat18ortalamaNo2=Saat18["NO2 ( µg/m³ )"].mean()

# O3 ortalama

Saat18ortalamaO3=Saat18["O3 ( µg/m³ )"].mean()

# CO ortalama

Saat18ortalamaCo=Saat18["CO ( µg/m³ )"].mean()


#-----------------------------------------------------------------------------#

# PM10 ortalama 

Saat00ortalamaPm10=Saat00["PM10 ( µg/m³ )"].mean()

# SO2 ortalama

Saat00ortalamaSo2=Saat00["SO2 ( µg/m³ )"].mean()

# NO2 ortalama

Saat00ortalamaNo2=Saat00["NO2 ( µg/m³ )"].mean()

# O3 ortalama

Saat00ortalamaO3=Saat00["O3 ( µg/m³ )"].mean()

# CO ortalama

Saat00ortalamaCo=Saat00["CO ( µg/m³ )"].mean()





#-----------------------------------------------------------------------------#


# Gösterme işlemleri

# PM10 Gösterimi

import matplotlib.pyplot as plt

saatler = ['08:00', '18:00', '00:00']
degerler = [Saat8ortalamaPm10, Saat18ortalamaPm10, Saat00ortalamaPm10]

f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler)
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.subplot(133)
plt.plot(saatler, degerler)
plt.suptitle('Valilik PM10 ( µg/m³ )')
plt.show()


#-----------------------------------------------------------------------------#

# SO2 Gösterimi

import matplotlib.pyplot as plt

saatler = ['08:00', '18:00', '00:00']
degerler = [Saat8ortalamaSo2, Saat18ortalamaSo2, Saat00ortalamaSo2]

f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler)
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.subplot(133)
plt.plot(saatler, degerler)
plt.suptitle('Valilik SO2 ( µg/m³ )')
plt.show()


#-----------------------------------------------------------------------------#

# NO2 Gösterimi

import matplotlib.pyplot as plt

saatler = ['08:00', '18:00', '00:00']
degerler = [Saat8ortalamaNo2, Saat18ortalamaNo2, Saat00ortalamaNo2]

f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler)
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.subplot(133)
plt.plot(saatler, degerler)
plt.suptitle('Valilik NO2 ( µg/m³ )')
plt.show()


#-----------------------------------------------------------------------------#

# O3 Gösterimi

import matplotlib.pyplot as plt

saatler = ['08:00', '18:00', '00:00']
degerler = [Saat8ortalamaO3, Saat18ortalamaO3, Saat00ortalamaO3]

f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler)
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.subplot(133)
plt.plot(saatler, degerler)
plt.suptitle('Valilik O3 ( µg/m³ )')
plt.show()

#-----------------------------------------------------------------------------#

# CO Gösterimi

import matplotlib.pyplot as plt

saatler = ['08:00', '18:00', '00:00']
degerler = [Saat8ortalamaCo, Saat18ortalamaCo, Saat00ortalamaCo]

f=plt.figure(figsize=(12,6))

plt.subplot(131)
plt.bar(saatler, degerler)
plt.subplot(132)
plt.scatter(saatler, degerler)
plt.subplot(133)
plt.plot(saatler, degerler)
plt.suptitle('Valilik CO ( µg/m³ )')
plt.show()



















