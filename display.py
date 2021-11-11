import cv2
import mediapipe as mp
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    cv2.imshow("Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
