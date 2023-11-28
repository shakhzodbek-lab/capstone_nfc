import cv2
import nfc

# Initialize the NFC reader
clf = nfc.ContactlessFrontend('usb')

# Initialize the face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to capture and detect faces
def detect_face():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow('Face Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# NFC event handler
def on_connect(tag):
    print("NFC Card Detected:", tag)
    detect_face()
    # Send data to the server here 

# Start the NFC event loop
try:
    clf.connect(rdwr={'on-connect': on_connect})
except KeyboardInterrupt:
    pass
finally:
    clf.close()
