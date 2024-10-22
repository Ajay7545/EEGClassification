# -*- coding: utf-8 -*-
"""model1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FJ38ybnvcmsIp9WJoMvrpqhjbXxDIE9s
"""

import time
import numpy as np
import os
from keras import layers, models, callbacks, regularizers, optimizers
from keras.layers import advanced_activations
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler as ms
import pandas as pd
import numpy as np
import numpy
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import matplotlib.pyplot as plt
import os
import glob
import datetime as dt

from datetime import timedelta
import numpy
import matplotlib.pyplot as plt
from pandas import read_csv
import pandas as pd
import math
from keras.callbacks import Callback
from keras.optimizers import adagrad, adam
from IPython.display import clear_output
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
import pywt

import tensorflow as tf
from tf.keras.models import Model
from tf.keras.layers import Dense, Activation, Permute, Dropout
from tf.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from tf.keras.layers import SeparableConv2D, DepthwiseConv2D
from tf.keras.layers import BatchNormalization
from tf.keras.layers import SpatialDropout2D
from tf.keras.regularizers import l1_l2
from tf.keras.layers import Input, Flatten
from tf.keras.constraints import max_norm
from tf.keras import backend as K

d1=pd.read_csv('d1.csv')
d1.head(1)

d1=d1[:300000]
len(d1)



d1.drop(['Unnamed: 0'],axis=1,inplace=True)
d1.head(1)

dy1=d1['Case'].values
y1=list(dy1)

d1.drop(['Case'], axis = 1, inplace = True)

x=d1.iloc[:].values
len(x)
x.shape

x=x.reshape(1200,12,250)

y=[]

for i in y1:
  if i==2.0:
    y.append(1)
  else:
    y.append(0)

i=0
w=[]
m=0
while (i<len(y)):
  j=y[i]
  i=i+1
  k=1
  while(y[i]==j):
    i=i+1
    k=k+1
    if(i==len(y)):
      break
  
  w.append(k)
  m=m+1
  i=i+1
  #print(m)

i=0
m=0
y2=[]
while(i<len(w)):
  j=w[i]
  c=int(j/250)
  k=0
  while(k<c):
    a=y[m]
    y2.append(a)
    k=k+1
  i=i+1
  m=m+j

x.shape

y2=np.asarray(y2)

X_train=x[0:960]
y_train=y2[0:960]
X_test=x[960:,]
y_test=y2[960:,]

y_train.shape

X_train=X_train.reshape(X_train.shape[0],1,12,250)
X_test=X_test.reshape(X_test.shape[0],1,12,250)



input1   = tf.keras.layers.Input(shape = (1, 12, 250))
block1       = tf.keras.layers.Conv2D(8, (1, 64), padding = 'same', input_shape = (1, 12,250),use_bias = False,data_format='channels_last')(input1)
#block1 = tf.keras.layers.BatchNormalization(axis = 1)(block1)
block1       = tf.keras.layers.DepthwiseConv2D((1, 12), use_bias = False,  depth_multiplier = 2,depthwise_constraint = tf.keras.constraints.max_norm(1.))(block1)
#block1 = tf.keras.layers.BatchNormalization(axis = 1)(block1)
block1 = tf.keras.layers.Activation('elu')(block1)
block1 = tf.keras.layers.AveragePooling2D((1, 1))(block1)
block1 = tf.keras.layers.Dropout(0.5)(block1)

block2       = tf.keras.layers.SeparableConv2D(16, (1, 16),use_bias = False, padding = 'same')(block1)
#block2       = tf.keras.layers.BatchNormalization(axis = 1)(block2)
block2       = tf.keras.layers.Activation('elu')(block2)
block2       = tf.keras.layers.AveragePooling2D((1, 1))(block2)
block2       = tf.keras.layers.Dropout(0.5)(block2)

flatten      = tf.keras.layers.Flatten(name = 'flatten')(block2)

dense        = tf.keras.layers.Dense(1, name = 'dense', kernel_constraint = tf.keras.constraints.max_norm(0.25))(flatten)
softmax      = tf.keras.layers.Activation('sigmoid', name = 'softmax')(dense)

softmax.shape

model=tf.keras.Model(inputs=input1, outputs=softmax)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics = ['accuracy'])

filepath="waveletsweights.best.hdf50"

#checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='auto')

early_stopping_monitor = EarlyStopping(monitor='val_loss', patience=5, verbose=1, mode='auto')
callbacks_list = [checkpoint]

print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)
type(y_test)
t=y_test
t=list(t)
#print(t)
t.append(1)
t.append(1)

y_test=np.asarray(t)
y_test.shape

print(X_test.shape)
print(y_test.shape)

#!pip install tensorflow

fittedModel = model.fit(X_train, y_train, batch_size = 16, epochs = 1000,verbose = 1,validation_data=(X_test, y_test))

plt.plot(fittedModel.history['acc'])
plt.plot(fittedModel.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')

plt.show()
# summarize history for loss
plt.plot(fittedModel.history['loss'])
plt.plot(fittedModel.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train'], loc='upper left')
plt.show()

