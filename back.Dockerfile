FROM ubuntu:20.04

RUN apt update -y && apt upgrade -y && apt install -y gnupg2

RUN apt-key adv --fetch-keys  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub

RUN bash -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list'

RUN apt update -y

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install python3 python3-pip python3-matplotlib cuda-cudart-10-1 libgl1-mesa-glx libglib2.0-0 -y

RUN pip3 install --upgrade pip && pip3 install --upgrade setuptools

RUN pip3 install tensorflow-cpu && pip3 install keras

RUN pip3 install matplotlib && pip3 install opencv-python

RUN pip3 install Flask && pip3 install -U flask-cors

ENV CUDA_VISIBLE_DEVICES=""

COPY ./backend /backend

EXPOSE 5000/tcp

WORKDIR /backend

ENTRYPOINT ["python3", "upload_image.py"]
