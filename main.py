import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def take_and_save_screenshot():
    if frame is not None:
        cv2.imwrite("screenshot.png", frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detector', frame)

    key = cv2.waitKey(1) & 0xFF  # Capture the key press once

    if key == ord('q') or key == ord('Q'):
        break  # Exit the loop if 'q' or 'Q' is pressed
    elif key == ord('h') or key == ord('H'):
        take_and_save_screenshot()  # Take screenshot if 'h' or 'H' is pressed

cap.release()
cv2.destroyAllWindows()
