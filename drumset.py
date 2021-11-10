import cv2
img = cv2.imread("drumset.jpg")
img_re = cv2.resize(img,(int(img.shape[0]*2),int(img.shape[1])))
cv2.imshow("drums",img_re)
key = cv2.waitKey(10000)
#if key == ord('q'):
cv2.destroyAllWindows()
