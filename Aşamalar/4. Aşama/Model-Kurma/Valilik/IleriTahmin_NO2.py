# Kütüphanelerin eklenmesi

import pandas as pd
import numpy as np

# Veri setlerinin yüklenmesi

veri = pd.read_excel("Valilik.xlsx")

# Tarih veri tipinin index tarafına aktarılması

veri["Tarih"] = pd.to_datetime(veri["Tarih"])
veri.index=veri.Tarih

# Elimizde olan veri ile NO2 grafiği çizilmesi

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(50,10))
veri.NO2.plot(label='NO2')
plt.title('NO2 Günlük Dağılımı', fontsize=20)
plt.show()

# NO2 verisinin standartlaştırılması(0-1)

from sklearn.preprocessing import MinMaxScaler
values = veri['NO2'].values.reshape(-1,1)
values = values.astype('float32')
scaler = MinMaxScaler(feature_range=(0, 1))
fitveri = scaler.fit_transform(values)

# Veri setinde %60 eğitim %40 test

TRAIN_SIZE = 0.60
train_size = int(len(fitveri) * TRAIN_SIZE)
test_size = len(fitveri) - train_size
train, test = fitveri[0:train_size, :], fitveri[train_size:len(fitveri), :]

# Her okumadan sonra tahmin edilip Yeni veriseti oluşturulması

def yeni_veriseti(data, standart = 1):
    data_X, data_Y = [], []
    for i in range(len(data) - standart - 1):
        a = data[i:(i + standart), 0]
        data_X.append(a)
        data_Y.append(data[i + standart, 0])
    return(np.array(data_X), np.array(data_Y))

# Orjinal eğitim verisi 
window_size = 1
train_X, train_Y = yeni_veriseti(train, 1)
test_X, test_Y = yeni_veriseti(test, 1)

# Yeni eğitim verisi oluşturulması

train_X = np.reshape(train_X, (train_X.shape[0], 1, train_X.shape[1]))
test_X = np.reshape(test_X, (test_X.shape[0], 1, test_X.shape[1]))

# Modelin Kurulması - Tek katmanlı LSTM

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,LSTM

def fit_model(train_X, train_Y, window_size = 1):
    model = Sequential()
    model.add(LSTM(100, 
                   input_shape = (1, window_size)))
    model.add(Dense(1))
    model.compile(loss = "mean_squared_error", 
                  optimizer = "adam")
    model.fit(train_X, 
              train_Y, 
              epochs = 250, 
              batch_size = 1, 
              verbose = 1)
    
    return(model)
# Fit the first model.
Son_model = fit_model(train_X, train_Y, window_size)

# Tahmin değerinin görüntülenmesi

import math
from sklearn.metrics import mean_squared_error
def Tahmin_Skoru(model, X, Y):
    pred = scaler.inverse_transform(model.predict(X))
    orig_data = scaler.inverse_transform([Y])
    score = math.sqrt(mean_squared_error(orig_data[0], pred[:, 0]))
    return(score, pred)
    
rmse_train, train_predict = Tahmin_Skoru(Son_model, train_X, train_Y)
rmse_test, test_predict = Tahmin_Skoru(Son_model, test_X, test_Y)
print("Eğitim Verisi Skoru: %.2f rmse" % rmse_train)
print("Test Verisi Skoru:: %.2f rmse" % rmse_test)

# Öğrenilen değerlerin tahmini

train_predict_plot = np.empty_like(fitveri)
train_predict_plot[:, :] = np.nan
train_predict_plot[window_size:len(train_predict) + window_size, :] = train_predict

# Test verisi tahmini

test_predict_plot = np.empty_like(fitveri)
test_predict_plot[:, :] = np.nan
test_predict_plot[len(train_predict) + (window_size * 2) + 1:len(fitveri) - 1, :] = test_predict

# Değerlerin grafikte gösterimi

import matplotlib.pyplot as plt
plt.figure(figsize = (40, 10))
plt.plot(scaler.inverse_transform(fitveri), label = "Orjinal Değerler")
plt.plot(train_predict_plot, label = "Eğitim veri seti tahmini")
plt.plot(test_predict_plot, label = "Test veri seti tahmini")
plt.xlabel("Günler")
plt.ylabel("NO2 Değişimi")
plt.title("Gerçek Ve Tahmin değerlerinin Karşılaştırılması")
plt.legend()
plt.show()
