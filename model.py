import tensorflow.keras as kr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://raw.githubusercontent.com/ianmcloughlin/2020A-machstat-project/master/dataset/powerproduction.csv', names=['speed', 'power'] , skipinitialspace=True, skiprows=1, engine="python")
data_copy = dataset.copy()

x_train = data_copy.pop('speed')
y_train = data_copy.pop('power')

# Train a different model.
model = kr.models.Sequential()

model.add(kr.layers.Flatten()) 
model.add(kr.layers.Dense(50, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.add(kr.layers.Dense(25, input_shape=(1,), activation='sigmoid', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.add(kr.layers.Dense(1, activation='linear', kernel_initializer="glorot_uniform", bias_initializer="glorot_uniform"))
model.compile(kr.optimizers.Adam(lr=0.001), loss='mean_squared_error')

model.fit(x_train, y_train, epochs=600, batch_size=10)

plt.plot(x_train, y_train, label='actual')
plt.plot(x_train, model.predict(x_train), label='prediction')
plt.legend()

# save the model to disk
model.save('models\model')