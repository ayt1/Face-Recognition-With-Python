# Face-Recognition-With-Python
Face recognition using Dlib deep learning based face embedding model and face_recognition python library

## Required Libraries
- Dlib

- face_recognition

If you want to use your GPU for faster processing, install Dlib with GPU support. You can also benefit from Dlib GUI feautures with GPU support enabled.

For further details about installiation process, refer to here http://dlib.net/compile.html

face_recognition library can be installed using 'pip install face_recognition'. More information:

https://github.com/ageitgey/face_recognition

## Dataset Preparation
In order to get face images, I have used this python script https://github.com/hardikvasa/google-images-download

In this project, I only focused on recognizing Samuel Jackson's face but you can do multiple face recognition.

After download, delete inappropriate images(images not containing Samuel Jackson etc) since they may cause misrecognition.

## Run .py Files
Run encode_faces.py first to obtain face encodings corresponding to each image in your train folder. (There is no training involved in the code. The model has already been trained. I am using the name 'train' just for convenience.)

Afterwards, run face_recognition.py on your test images to see whether you success. Dont forget to change path names given as 'example' with your own paths. You can use the same script mentioned above to get your test images. I merged my test images using this website https://www.photojoiner.net/ to test them all at once. 

It is possible to do real time face recognition if you have suitable hardware equipment. Since I dont have GPU on my laptop, I tested the model on images.
