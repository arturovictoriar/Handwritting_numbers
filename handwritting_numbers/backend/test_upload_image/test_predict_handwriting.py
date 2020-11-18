#!/usr/bin/env python3

from keras.datasets import mnist
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
import keras.models
from keras.utils import to_categorical

# Import the model 
model = keras.models.load_model('mymodel')
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# reshape the test samples
x_test = x_test.reshape(10000,28,28,1)

# Image to predict
img_predict = x_test[90]

# Prediction a image with the model
prediction = model.predict_classes(img_predict.reshape(1,28,28,1))

# Plotting the image predicted
plt.imshow(img_predict)
plt.title("The number predicted was: {}".format(prediction))
plt.show()
print("\n\n\nThe number predicted was: ", prediction)

img_predict = imread("5gb.jpg")
img_predict = 255 - img_predict
image = img_predict
image = image.astype('float32')
image = image.reshape(1, 28, 28, 1)
#image /= 255

# Prediction a image with the model
prediction = model.predict_classes(image)

# Plotting the image predicted
plt.imshow(img_predict)
plt.title("The number predicted was: {}".format(prediction))
plt.show()
print("\n\n\nThe number predicted was: ", prediction)
