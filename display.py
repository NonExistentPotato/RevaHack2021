import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    cv2.imshow("Display",img)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
