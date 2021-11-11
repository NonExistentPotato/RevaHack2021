import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector


def landing_screen(hands, img):
    img, bbox = cvzone.putTextRect(img,"Welcome To Non-Existent Bank",[100,200],2,3,offset=50,
                 colorB=(255,255,255))
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
    img , bbox7 = cvzone.putTextRect(img,"7",[150,350],1,2,offset=40, colorB=(255,255,255))
    img , bbox8 = cvzone.putTextRect(img,"8",[250,350],1,2,offset=40, colorB=(255,255,255))
    img , bbox9 = cvzone.putTextRect(img,"9",[350,350],1,2,offset=40, colorB=(255,255,255))

    img , bbox4 = cvzone.putTextRect(img,"4",[150,450],1,2,offset=40, colorB=(255,255,255))
    img , bbox5 = cvzone.putTextRect(img,"5",[250,450],1,2,offset=40, colorB=(255,255,255))
    img , bbox6 = cvzone.putTextRect(img,"6",[350,450],1,2,offset=40, colorB=(255,255,255))

    img , bbox1 = cvzone.putTextRect(img,"1",[150,550],1,2,offset=40, colorB=(255,255,255))
    img , bbox2 = cvzone.putTextRect(img,"2",[250,550],1,2,offset=40, colorB=(255,255,255))
    img , bbox3 = cvzone.putTextRect(img,"3",[350,550],1,2,offset=40, colorB=(255,255,255))

    img , bboxx = cvzone.putTextRect(img,"X",[150,650],1,2,offset=40, colorB=(255,255,255))
    img , bbox0 = cvzone.putTextRect(img,"0",[250,650],1,2,offset=40, colorB=(255,255,255))
    img , bboxe = cvzone.putTextRect(img,"<-",[350,650],1,2,offset=40, colorB=(255,255,255))

    buttonList = [bboxe,bbox0,bbox1,bbox2,bbox3,bbox4,bbox5,bbox6,bbox7,bbox8,bbox9,bboxx]
    return (img, buttonList)

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
    img , bbox = cvzone.putTextRect(img,"Enter PIN",[100,200],1,2,offset=50,border=5, colorB=(255,255,255))
    img , buttonList = draw_keypad(img)
    if hands:
        for button in buttonList:
            x=button[0]
            y=button[1]
            w=button[2]
            h=button[3]
            lmList = hands[0]['lmList']
            cursor = lmList[8]
            length, info = detector.findDistance(lmList[8],lmList[12])
            if length < 30:
                if x< cursor[0] <x+w and y< cursor[1] <y+h :
                    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), cv2.FILLED)
                    print("clicked!")


    cv2.imshow("Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
