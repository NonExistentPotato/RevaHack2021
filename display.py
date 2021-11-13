# IMPORT NECESSARY LIBRARIES AND MODULES
import cv2
import mediapipe as mp
import cvzone
from cvzone.HandTrackingModule import HandDetector
from time import sleep

# ACCESSING CAMERA FEED AND DETECTING HANDS
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon = 1, maxHands = 1)

# DEFINE CONSTANTS
keys = [['7','8','9'],['4','5','6'],['1','2','3'],['X','0','<-']]
PINtext = "PIN: "
AMTtext = "Amt: "

# FUNCTION TO DRAW NUMERIC KEYPAD ON DISPLAY
def drawKeyboard(img, buttonList):
    for button in buttonList:
        x,y = button.pos
        w,h = button.size
        cv2.rectangle(img, button.pos, (x+w,y+h), (255,0,255), cv2.FILLED)
        cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
    return img

# CLASS TO HELP WITH DRAWING KEYPAD
class Button():
    def __init__(self,pos,text,size=[85,85]):
        self.pos = pos
        self.text = text
        self.size = size
       
buttonList = []
for i in range(len(keys)):
        for j,k in enumerate (keys[i]):
            buttonList.append(Button([100 * j + 50, 100 * i +50], k))


"""def landingScreen(img):
    cv2.rectangle(img, (50,200), (900,300), (255,0,255), cv2.FILLED)
    cv2.putText(img, "Welcome to Non-Existent Bank", (80,260), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),5)
    cv2.rectangle(img, (350,400), (600,500), (255,0,255), cv2.FILLED)
    cv2.putText(img, "START", (380,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
    if lmList:
        l, _, _ = detector.findDistance(8,12,img, draw=False)
        x,y = (350,400)
        w,h = (600,500)
        if x< lmList[8][0] <w and y< lmList[8][1] <h:
            cv2.rectangle(img, (350,400), (600,500), (0,255,0), cv2.FILLED)
            cv2.putText(img, "START", (380,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5) 
            if l < 30:
                cv2.rectangle(img, (x,y), (w,h), (255, 255, 255), cv2.FILLED)
                print("clicked!")
    return (img)"""

"""def pinScreen(img, PINtext):
    img = drawKeyboard(img,buttonList)

    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            if x< lmList[8][0] <x+w and y< lmList[8][1] <y+h:
                cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                l, _, _ = detector.findDistance(8,12,img, draw=False)
                if l < 30:
                    cv2.rectangle(img, button.pos, (x+w,y+h), (255,255,255), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                    if button.text == "<-":
                        print("Next")
                        #img , AMTtext = 
                        #amtScreen()
                        screenNO = 2
                        return (img, PINtext)
                    else:
                        PINtext += button.text
                        sleep(2)
    cv2.rectangle(img, (50,500), (400,600), (255,0,255), cv2.FILLED)
    cv2.putText(img, PINtext, (80,580), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)"""

"""def amtScreen(img, AMTtext):
    img = drawKeyboard(img,buttonList)

    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            if x< lmList[8][0] <x+w and y< lmList[8][1] <y+h:
                cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                l, _, _ = detector.findDistance(8,12,img, draw=False)
                if l < 30:
                    cv2.rectangle(img, button.pos, (x+w,y+h), (255,255,255), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                    if button.text == "<-":
                        print("Next")
                        screenNO = 3
                        return (img, AMTtext)
                    else:
                        AMTtext += button.text
                        sleep(1)
    cv2.rectangle(img, (50,500), (400,600), (255,0,255), cv2.FILLED)
    cv2.putText(img, AMTtext, (80,580), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)"""

"""def completeScreen(img):
    cv2.rectangle(img, (50,200), (700,300), (255,0,255), cv2.FILLED)
    cv2.putText(img, "Transaction Complete !", (80,260), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),5)
    cv2.rectangle(img, (250,400), (500,500), (255,0,255), cv2.FILLED)
    cv2.putText(img, "CLOSE", (280,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
    if lmList:
        l, _, _ = detector.findDistance(8,12,img, draw=False)
        x,y = (250,400)
        w,h = (500,500)
        if x< lmList[8][0] <w and y< lmList[8][1] <h:
            cv2.rectangle(img, (250,400), (500,500), (0,255,0), cv2.FILLED)
            cv2.putText(img, "CLOSE", (280,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5) 
            if l < 30:
                cv2.rectangle(img, (x,y), (w,h), (255, 255, 255), cv2.FILLED)
                print("clicked!")
    return (img)"""

# WELCOME SCREEN
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    """screenNo = 0
    if screenNO == 0:
        img = landingScreen(img)
    elif screenNO == 1:
        img, PINtext = pinScreen(img, PINtext)
    elif screenNO == 2:
        img, AMTtext = amtScreen(img, AMTtext)
    elif screenNO == 3:
        img = completeScreen(img)"""
    cv2.rectangle(img, (50,200), (900,300), (255,0,255), cv2.FILLED)
    cv2.putText(img, "Welcome to Non-Existent Bank", (80,260), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),5)
    cv2.rectangle(img, (350,400), (600,500), (255,0,255), cv2.FILLED)
    cv2.putText(img, "START", (380,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
    if lmList:
        l, _, _ = detector.findDistance(8,12,img, draw=False)
        x,y = (350,400)
        w,h = (600,500)
        if x< lmList[8][0] <w and y< lmList[8][1] <h:
            cv2.rectangle(img, (350,400), (600,500), (0,255,0), cv2.FILLED)
            cv2.putText(img, "START", (380,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5) 
            if l < 30:
                cv2.rectangle(img, (x,y), (w,h), (255, 255, 255), cv2.FILLED)
                print("clicked!")
                break

    cv2.imshow("ATM Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

# SCREEN TO ENTER PIN
breakerP = False
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    
    img = drawKeyboard(img,buttonList)
    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            if x< lmList[8][0] <x+w and y< lmList[8][1] <y+h:
                cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                l, _, _ = detector.findDistance(8,12,img, draw=False)
                if l < 30:
                    cv2.rectangle(img, button.pos, (x+w,y+h), (255,255,255), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                    if button.text == "<-":
                        print("Next")
                        breakerP = True
                        break
                    else:
                        PINtext += button.text
                        sleep(1)
        if breakerP:
            break
    cv2.rectangle(img, (50,500), (400,600), (255,0,255), cv2.FILLED)
    cv2.putText(img, PINtext, (80,580), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)

    cv2.imshow("ATM Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows()

# SCREEN TO ENTER WITHDRAW AMOUNT
breakerA = False
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    img = drawKeyboard(img,buttonList)
    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            if x< lmList[8][0] <x+w and y< lmList[8][1] <y+h:
                cv2.rectangle(img, button.pos, (x+w,y+h), (0,255,0), cv2.FILLED)
                cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                l, _, _ = detector.findDistance(8,12,img, draw=False)
                if l < 30:
                    cv2.rectangle(img, button.pos, (x+w,y+h), (255,255,255), cv2.FILLED)
                    cv2.putText(img, button.text, (x+20,y+65), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
                    if button.text == "<-":
                        print("Next")
                        breakerA = True
                        break
                    else:
                        AMTtext += button.text
                        sleep(0.5)
        if breakerA:
            break
    cv2.rectangle(img, (50,500), (500,600), (255,0,255), cv2.FILLED)
    cv2.putText(img, AMTtext, (80,580), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)

    cv2.imshow("ATM Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows() 

# TRANSACTION COMPLETE SCREN
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    cv2.rectangle(img, (50,200), (700,300), (255,0,255), cv2.FILLED)
    cv2.putText(img, "Transaction Complete !", (80,260), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),5)
    cv2.rectangle(img, (250,400), (500,500), (255,0,255), cv2.FILLED)
    cv2.putText(img, "CLOSE", (280,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5)
    if lmList:
        l, _, _ = detector.findDistance(8,12,img, draw=False)
        x,y = (250,400)
        w,h = (500,500)
        if x< lmList[8][0] <w and y< lmList[8][1] <h:
            cv2.rectangle(img, (250,400), (500,500), (0,255,0), cv2.FILLED)
            cv2.putText(img, "CLOSE", (280,480), cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255),5) 
            if l < 30:
                cv2.rectangle(img, (x,y), (w,h), (255, 255, 255), cv2.FILLED)
                print("clicked!")
                sleep(0.5)
                break

    cv2.imshow("ATM Display",img)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
cv2.destroyAllWindows()