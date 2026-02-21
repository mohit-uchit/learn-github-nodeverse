import cv2
import pyautogui
import time
# Load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print('done')

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    status, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    if len(faces) > 0:
        # Draw rectangle around the first detected face
        (x, y, w, h) = faces[0]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        pyautogui.hotkey("win", "x")
        time.sleep(0.3)
        pyautogui.hotkey('u')
        time.sleep(0.3)
        pyautogui.hotkey('u')
    else:
        # Show "No face detected" text on the video window
        cv2.putText(img, "No face detected", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



    # Display the video feed (always running)
    cv2.imshow('Detected Face', img)

    # Break loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
