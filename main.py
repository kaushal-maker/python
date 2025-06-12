import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Step 1: Load Known Faces
path = 'images'
images = []
names = []
imageList = os.listdir(path)

for imgName in imageList:
    img = cv2.imread(f'{path}/{imgName}')
    images.append(img)
    names.append(os.path.splitext(imgName)[0])

# Step 2: Encode Faces
def findEncodings(images):
    encodings = []
    for img in images:
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(imgRGB)[0]
        encodings.append(encode)
    return encodings

knownEncodings = findEncodings(images)

# Step 3: Mark Attendance
def markAttendance(name):
    print(f"Marking attendance for: {name}")  # 🛠 Debug line
    try:
        with open('Attendance.csv', 'r+') as f:
            lines = f.readlines()
            nameList = [line.split(',')[0] for line in lines]
            if name not in nameList:
                now = datetime.now()
                timeStr = now.strftime('%H:%M:%S')
                dateStr = now.strftime('%Y-%m-%d')
                f.write(f'{name},{timeStr},{dateStr}\n')
                print("Attendance marked ✅")  # 🛠 Debug line
    except FileNotFoundError:
        with open('Attendance.csv', 'w') as f:
            f.write('Name,Time,Date\n')
            now = datetime.now()
            f.write(f'{name},{now.strftime("%H:%M:%S")},{now.strftime("%Y-%m-%d")}\n')
            print("Attendance.csv created and marked ✅")  # 🛠 Debug line


# Step 4: Start Webcam
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    smallFrame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgbSmallFrame = cv2.cvtColor(smallFrame, cv2.COLOR_BGR2RGB)

    faceLocations = face_recognition.face_locations(rgbSmallFrame)
    faceEncodings = face_recognition.face_encodings(rgbSmallFrame, faceLocations)

    for encodeFace, faceLoc in zip(faceEncodings, faceLocations):
        matches = face_recognition.compare_faces(knownEncodings, encodeFace)
        faceDis = face_recognition.face_distance(knownEncodings, encodeFace)

        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = names[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, name, (x1+6, y2+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            markAttendance(name)

    cv2.imshow('Face Attendance System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
