import os, random, shutil
import numpy as np
import pandas as pd
import PIL
#import keras
import itertools
from PIL import Image

import tensorflow as tf

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
#from skimage import feature, data, io, measure
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
#matplotlib inline 

import cv2
from tensorflow.keras import backend as K
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dropout, Flatten, Conv2D, MaxPooling2D, Dense, Activation
from tensorflow.keras.optimizers import RMSprop, Adam
from tensorflow.keras.layers import BatchNormalization
#from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping
from keras.utils import np_utils
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from tensorflow.keras.callbacks import TensorBoard
import io
import time
import datetime
from tensorflow.keras.optimizers import Adam,Adadelta
from tensorflow.keras.preprocessing.image import ImageDataGenerator


batch_size_train = 25
num_classes= 5
IMAGE_SIZE=[200,200]
classes_required = ['young', 'middle1', 'middle2', 'middel3', 'old']


datagen = ImageDataGenerator(rescale=1.0/255.0)

train_path = '/Users/ruisantos/Desktop/ano4/aa/project2/heartbeat/photos2/'
train_batches = datagen.flow_from_directory(train_path, target_size=(200,200), classes=classes_required, batch_size=batch_size_train)

model=Sequential()
model.add(Conv2D(16,kernel_size=(3,3), activation="relu" ,input_shape=IMAGE_SIZE + [3], padding='same'))

model.add(Conv2D(32, kernel_size=(3,3), activation="relu",padding='same'))
model.add(BatchNormalization()) 
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.30))

model.add(Conv2D(64, kernel_size=(3,3), activation="relu",padding='same'))
#model.add(BatchNormalization()) 
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.35))

model.add(Conv2D(128, kernel_size=(3,3), activation="relu",padding='same'))
#model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization()) 
model.add(Dropout(0.45))

model.add(Flatten())
model.add(Dense(64, activation="relu"))
model.add(Dense(num_classes, activation="softmax"))


opt = Adadelta(learning_rate=0.0001, decay=1e-6)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])


model.fit(train_batches, steps_per_epoch=50, epochs=100, verbose=1)

