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




#plt.figure(figsize=(12,6))
#
#plt.plot(veri1.Tarih,veri1["SO2 ( µg/m³ )"],color="red",linewidth=2,linestyle="--",marker="o") 
#
#plt.xlabel("Tarih")
#
#plt.ylabel("SO2")
#
#plt.title("Türkiye'nin SO2 Oranları")
#
#plt.show()
'''
plt.figure(figsize=(16,10))

plt.plot(veri2.Tarih,
        veri2["PM10 ( µg/m³ )"],
         color="r",
         linewidth=1,
         alpha=0.5)

plt.plot(veri2.Tarih,
        veri2["SO2 ( µg/m³ )"],
        color="blue",
        linewidth=1,

        alpha=0.9)

plt.plot(veri2.Tarih,
        veri2["CO ( µg/m³ )"],
        color="green",
        linewidth=1,
        alpha=0.9)

plt.plot(veri2.Tarih,
        veri2["NO2 ( µg/m³ )"],
        color="#0ea7b5",
        linewidth=1,
        alpha=0.9)

plt.plot(veri2.Tarih,
        veri2["O3 ( µg/m³ )"],
        color="#0c457d",
        linewidth=1,
         alpha=0.9)




plt.xlabel("Tarih")

plt.ylabel("( µg/m³ )")

plt.title("Adana Hava Ölçüm Sonuçları Aralık ve Ocak")

plt.show()

""""
plt.hist([veri1.Tarih,veri1["SO2 ( µg/m³ )"]],
         color=['#0c457d','#0ea7b5'],
         label=["Tarih","SO2 ( µg/m³ )"])

plt.xlabel("Oranlar")

plt.ylabel("Dağılımlar")
plt.title("İşsizlik ve Enflasyon Oranları")
plt.legend()
plt.show()
"""

veri1.Tarih = pd.to_datetime(veri1.Tarih)
veri1.set_index('Tarih', inplace=True)




plt.hist([veri2["PM10 ( µg/m³ )"],veri2["SO2 ( µg/m³ )"],veri2["CO ( µg/m³ )"],veri2["NO2 ( µg/m³ )"],veri2["O3 ( µg/m³ )"]],
         color=['red','blue','green','#0c457d','#0ea7b5'],
         label=["PM10 ( µg/m³ )","SO2 ( µg/m³ )","CO ( µg/m³ )","NO2 ( µg/m³ )","O3 ( µg/m³ )"])

plt.xlabel("Oranlar")

plt.ylabel("Dağılımlar")
plt.title("İşsizlik ve Enflasyon Oranları")
plt.legend() 
plt.show()






plt.figure(figsize=(10,12))

plt.bar(veri2.Tarih,veri2["PM10 ( µg/m³ )"],label="PM10",width=0.4,color="red")
plt.bar(veri2.Tarih,veri2["SO2 ( µg/m³ )"],label="SO2",color="blue")
plt.bar(veri2.Tarih,veri2["CO ( µg/m³ )"],label="CO",color="green")
plt.bar(veri2.Tarih,veri2["NO2 ( µg/m³ )"],label="NO2",color="#0c457d")
plt.bar(veri2.Tarih,veri2["O3 ( µg/m³ )"],label="O3",color="#0ea7b5")


plt.ylabel("Oran")
plt.xlabel("Tarih")
plt.legend()
plt.title("Hava durumu")
plt.show()

'''

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

plt.figure(figsize=(10,12))

plt.bar(veri2.Tarih,veri2["PM10 ( µg/m³ )"],label="PM10",width=0.4,color="red")
plt.bar(veri2.Tarih,veri2["SO2 ( µg/m³ )"],label="SO2",color="blue")



plt.ylabel("Oran")
plt.xlabel("Tarih")
plt.legend()
plt.title("Hava durumu")
plt.show()

















































