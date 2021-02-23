#!/usr/bin/env python3

"""
    Identifying handwriting numbers images with keras,
    using convolutional NN, relu active funtcion,
    crossentropy loss function and adam optimizer
"""

from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

#parse the training and testing datasets from the database
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#reshaping data to fit model shape(samples, height_in, weight_in, layers)
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)

#converting the data to a one-hot encode target column
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#creating the model
model = Sequential()

#adding the model layers 4 layers
model.add(Conv2D(64, kernel_size=3, activation='relu', input_shape=(28,28,1)))
model.add(Conv2D(32, kernel_size=3, activation='relu'))
model.add(Flatten())
model.add(Dense(10, activation='softmax'))

#compiling the model using adam optimizer and crossentropy loss function
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#training the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)

#saving the model in the current folder
model.save('mymodel')
