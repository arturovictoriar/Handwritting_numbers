#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
from flask import request, redirect
import os
app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "/root/upload_image/uploaded_ima"


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print(image)
            return {"status": "Ok"}
    return {9:1}

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=80)
