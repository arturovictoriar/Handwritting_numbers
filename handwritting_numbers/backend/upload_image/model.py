#!/usr/bin/env python3

import cv2 as cv
import keras.models

def pred(content_image):
    # Import the model 
    model = keras.models.load_model('mymodel')

    image = content_image
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.threshold(image, 130, 255, cv.THRESH_BINARY)[1]    
    image = cv.resize(image, (28,28))
    image = 255 - image
    image = image.astype('float32')
    image = image.reshape(1, 28, 28, 1)
    
    # Image to predict
    print(image.shape)

    # Prediction a image with the model
    prediction = model.predict_classes(image)

    # Plotting the image predicted
    print("\n\n\nThe number predicted was: ", prediction)
    return prediction

#pred(content_image = imread("uploaded_ima/rsz_31.jpg").reshape(28,28,1))
