FROM python:latest
LABEL authors="Adam"

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python pillow numpy matplotlib

CMD  ["/bin/bash"]