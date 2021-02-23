#!/usr/bin/env python3

from keras.datasets import mnist
import matplotlib.pyplot as plt
import keras.models
from keras.utils import to_categorical

model = keras.models.load_model('mymodel')

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000,28,28,1)
y_test = to_categorical(y_test)

# Evaluating the model on the test data using `evaluate`
print("\n\n\nEvaluate on test data")
results = model.evaluate(x_test, y_test, batch_size=128)
print("\n\n\nTest loss: ", results[0])
print("Test accuracy: ", results[1])
