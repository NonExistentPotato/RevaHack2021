import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector


def landing_screen(hands, img):
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
                cv2.rectangle(img, (x1,x2), (y1,y2), (255, 255, 255), cv2.FILLED)
                print("clicked!")
                return 0

def draw_keypad(img):
    img , bbox = cvzone.putTextRect(img,"7",[150,350],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"8",[250,350],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"9",[350,350],1,2,offset=40,border=5, colorB=(255,255,255))

    img , bbox = cvzone.putTextRect(img,"4",[150,450],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"5",[250,450],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"6",[350,450],1,2,offset=40,border=5, colorB=(255,255,255))

    img , bbox = cvzone.putTextRect(img,"1",[150,550],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"2",[250,550],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"3",[350,550],1,2,offset=40,border=5, colorB=(255,255,255))

    img , bbox = cvzone.putTextRect(img,"X",[150,650],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"0",[250,650],1,2,offset=40,border=5, colorB=(255,255,255))
    img , bbox = cvzone.putTextRect(img,"<-",[350,650],1,2,offset=40,border=5, colorB=(255,255,255))

    return img

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon = 1, maxHands = 1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img, flipType=False)

    #landing_screen(hands, img)

    #lmList, bboxInfo = detector.findPosition(img)
    img , bboxx = cvzone.putTextRect(img,"Enter PIN",[100,200],1,2,offset=50,border=5, colorB=(255,255,255))
    img = draw_keypad(img)
    

    cv2.imshow("Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
