#!/usr/bin/python3

""" API REST for Digitalize an image """

# import libraries and modules
from flask import Flask
from flask import request, redirect
from model import pred
import numpy as np
import os
import cv2 as cv
from flask_cors import CORS

# create an web app socker using flask
app = Flask(__name__)
# set up a path for store the images
app.config["IMAGE_UPLOADS"] = "/backend/uploaded_ima"
# allow cors
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    """ Digitalize an image number """
    if request.method == "POST":
        if request.files:
            # get and save the image in the given folder
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], "temp"))
            try:
                # get the image digitalized
                r = pred(cv.imread("uploaded_ima/temp"))
            except Exception as e:
                print(e)
                r = None
            print(type(r))
            # remove the current imagen of the server
            os.remove("/backend/uploaded_ima/temp")
            print(image)
            # if the given image was digitalized send a json the number predicted
            # else send a json indicating the server was not able to predict the given image
            if r:
            	return {"status": "Ok", "Number_predicted":(r.tolist())[0]}
            return {"status": "Error", "Message": "the system can not identified the image"}
    return {"status": "running"}

@app.route('/', strict_slashes=False)
def hello_client():
    """ Prints a Message when / is called """
    return 'Server up and runnnig!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
