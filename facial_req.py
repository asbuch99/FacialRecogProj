from imutils.video import VideoStream
import face_recognition
import imutils
import pickle
import time
import cv2

#Initialize 'currentname' to trigger only when a new person is identified.
currentname = "unknown"

encodingsP = "encodings.pickle"

# load the known faces and embeddings

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# src = 0 : I had to set it to 0 in order to use the USB webcam attached to my laptop
vs = VideoStream(src=0, framerate=10).start()

time.sleep(2.0)

# loop over frames from the video file stream
for x in range(0, 4):

  frame = vs.read()
  frame = imutils.resize(frame, width=500)
  # Detect the face boxes
  boxes = face_recognition.face_locations(frame)
  encodings = face_recognition.face_encodings(frame, boxes)
  names = []

  # loop over the facial embeddings
  for encoding in encodings:
    # attempt to match each face in the input image to our known
    matches = face_recognition.compare_faces(data["encodings"], encoding)
    name = "Unknown"

    # check to see if we have found a match
    if True in matches:
      matchedIdxs = [i for (i, b) in enumerate(matches) if b]
      counts = {}

      # loop over the matched indexes and maintain a count for
      # each recognized face face
      for i in matchedIdxs:
        name = data["names"][i]
        counts[name] = counts.get(name, 0) + 1

      name = max(counts, key=counts.get)

      #If someone in dataset is identified, print their name on the screen
      if currentname != name:
        currentname = name
        print(currentname)

    # update the list of names
    names.append(name)

  # loop over the recognized faces
  for ((top, right, bottom, left), name) in zip(boxes, names):
    # draw the predicted face name on the image - color is in BGR
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 225), 2)
    y = top - 15 if top - 15 > 15 else top + 15
    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, .8,
                (0, 255, 255), 2)

  # display the image to our screen
  #cv2.imshow("Facial Recognition is Running", frame)
  key = cv2.waitKey(1) & 0xFF

# cleanup for memory
cv2.destroyAllWindows()
vs.stop()
