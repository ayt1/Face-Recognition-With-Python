from imutils import paths
import face_recognition
import pickle
import cv2

# get all training image paths from folder
imagePaths = list(paths.list_images('/path/name_of_the_folder')) # type your own path

# initialize encoding and name lists
trainEncodings = []
trainNames = []


for (i, imagePath) in enumerate(imagePaths):
    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # detect faces and get corresponding encoding for each face 
    boxes = face_recognition.face_locations(rgb, model="cnn",number_of_times_to_upsample=0)
    encodings = face_recognition.face_encodings(rgb, boxes)
    
    for encoding in encodings:
        trainEncodings.append(encoding)
        trainNames.append("Samuel_Jackson")

# store face encodings in a pickle file
data = {"encodings": knownEncodings, "names": knownNames}
f = open('/path/example.pickle', "wb") # type your own path
f.write(pickle.dumps(data))
f.close()


