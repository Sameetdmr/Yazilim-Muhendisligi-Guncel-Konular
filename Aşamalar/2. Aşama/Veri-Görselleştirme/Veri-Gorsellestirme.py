# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:15:00 2020

@author: samed
"""

import pandas as pd

import matplotlib.pyplot as plt


from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

##Çatalan veri seti eklenmesi
veri1=pd.read_excel("C:/Users/samed/Desktop/Yazilim-Muhendisligi-Guncel-Konular/Yazilim-Muhendisligi-Guncel-Konular/Adana-Çatalan-Günlük.xlsx")
son_veri1=veri1.drop('Tarih',1)
##Valilik veri seti eklenmesi
veri2=pd.read_excel("C:/Users/samed/Desktop/Yazilim-Muhendisligi-Guncel-Konular/Yazilim-Muhendisligi-Guncel-Konular/Adana-Valilik-Günlük.xlsx")
son_veri2 = veri2.drop('Tarih', 1)

########################################################################################



'''


Valilik Data Set Görselleştirme

''' 
'''


So2 Oranı 

f=plt.figure(figsize=(12,6))

plt.bar(veri2.Tarih,veri2["SO2 ( µg/m³ )"],width=0.5,
        color="#f05131",label="So2")

plt.ylabel("So2 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("So2 Dağılım Oranı")
plt.show()

'''
'''
No2 Oranı
 
f=plt.figure(figsize=(12,6))

plt.bar(veri2.Tarih,veri2["NO2 ( µg/m³ )"],width=0.5,
        color="#f9af2b",label="No2")

plt.ylabel("No2 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("No2 Dağılım Oranı")
plt.show()

'''
'''
PM10 Oranı

f=plt.figure(figsize=(12,6))

plt.bar(veri2.Tarih,veri2["PM10 ( µg/m³ )"],width=0.5,
        color="#98F5FF",label="PM10")

plt.ylabel("PM10 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("PM10 Dağılım Oranı")
plt.show()

'''
'''
Co oranı

f=plt.figure(figsize=(12,6))

plt.bar(veri2.Tarih,veri2["CO ( µg/m³ )"],width=0.5,
        color="#CD1076",label="CO")

plt.ylabel("CO Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("CO Dağılım Oranı")
plt.show()


'''
'''

O3 Oranı

f=plt.figure(figsize=(12,6))

plt.bar(veri2.Tarih,veri2["O3 ( µg/m³ )"],width=0.5,
        color="#228B22",label="O3")

plt.ylabel("O3 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("O3 Dağılım Oranı")
plt.show()

'''

###################################################################################

''' Catalan Data Set Görselleştirme '''

'''
SO2 ORANI

f=plt.figure(figsize=(12,6))

plt.bar(veri1.Tarih,veri1["SO2 ( µg/m³ )"],width=0.5,
        color="#f05131",label="So2")

plt.ylabel("So2 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("So2 Dağılım Oranı")
plt.show()

'''

'''
No2 Oranı
 
f=plt.figure(figsize=(12,6))

plt.bar(veri1.Tarih,veri1["NO2 ( µg/m³ )"],width=0.5,
        color="#f9af2b",label="No2")

plt.ylabel("No2 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("No2 Dağılım Oranı")
plt.show()

'''
'''
PM10 Oranı

f=plt.figure(figsize=(12,6))

plt.bar(veri1.Tarih,veri1["PM10 ( µg/m³ )"],width=0.5,
        color="#98F5FF",label="PM10")

plt.ylabel("PM10 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("PM10 Dağılım Oranı")
plt.show()

'''
'''
O3 Oranı

f=plt.figure(figsize=(12,6))

plt.bar(veri1.Tarih,veri1["O3 ( µg/m³ )"],width=0.5,
        color="#228B22",label="O3")


plt.ylabel("O3 Oranı")
plt.xlabel("Tarih")
plt.legend()
plt.title("O3 Dağılım Oranı")
plt.show()

'''
















































