import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon = 1, maxHands = 1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    img, bbox = cvzone.putTextRect(img,"Welcome To Non-Existent Bank",[100,200],2,3,offset=50,
    border=5, colorB=(255,255,255))
    img, bbox_start= cvzone.putTextRect(img,"START",[350,500],1,2,offset=50, border=5,colorB=(255,255,255))

    if hands:
        lmList = hands[0]['lmList']
        cursor = lmList[8]
        length, info = detector.findDistance(lmList[8],lmList[12])
        x1,x2,y1,y2 = bbox_start
        if length < 30:
            
            if x1< cursor[0] <x2 and y1< cursor[1] <y2:
                cv2.rectangle(img, (x1,y1), (x2,y2), (255, 255, 255), cv2.FILLED)
                print("clicked!")


    cv2.imshow("Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
