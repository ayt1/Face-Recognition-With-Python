import face_recognition
import pickle
import cv2

# read the pickle file we got from encode_faces.py
data = pickle.loads(open('/path/example.pickle', "rb").read()) # type your own path to pickle file

image = cv2.imread('/path/example.jpg') # read an image to test
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# the same steps as we did in encode_faces.py 
boxes = face_recognition.face_locations(rgb, number_of_times_to_upsample=0, model="cnn")
encodings = face_recognition.face_encodings(rgb, boxes)
 
# initialize the list of names for each face detected
names = []

for encoding in encodings:
    # attempt to match each face in the input image to our known
    # encodings
    matches = face_recognition.compare_faces(data["encodings"],encoding)
    name = "Unknown"
    
    # match detected
    if True in matches:
        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
        counts = {}
        
        for i in matchedIdxs:
            name = data["names"][i]
            counts[name] = counts.get(name, 0) + 1
            
        name = max(counts, key=counts.get)
        
    names.append(name)    

for ((top, right, bottom, left), name) in zip(boxes, names):
    # draw the predicted face name on the image
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
#show the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


