#!/bin/sh
#Identify handwritten image using Tensoflow-Keras in CPU
#Python version >= 3.5
#Systems: Ubuntu 16.04.7 LTS - Ubuntu 20.04.1 LTS

#update and upgrade Ubuntu
sudo apt update -y
sudo apt upgrade -y

#install python3, pip, keras, cuda, matplotlib and tensorflow cpu
sudo apt install python3 python3.pip -y
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade setuptools
sudo pip3 install tensorflow-cpu
sudo pip3 install keras
sudo apt install python3-matplotlib -y
sudo apt install cuda-cudart-10-1 -y
sudo pip3 install matplotlib
sudo pip3 install opencv-python
sudo apt install libgl1-mesa-glx -y

# set the CPU
export CUDA_VISIBLE_DEVICES=""

#install Flask
sudo pip3 install Flask

# start the service
./upload_image.py
