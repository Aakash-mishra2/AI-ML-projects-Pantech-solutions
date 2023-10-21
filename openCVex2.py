import cv2
import imutils
img = cv2.imread("sample1.JPG")
# resizeImg = imutils.resize(img,width=20)
# cv2.imwrite("resizedImg.JPG",resizeImg)
guassianBlur = cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("BlurLogo.JPG",guassianBlur);
# cv2.rectangle(src, startpoint, endpoint, color, thickness)
tImg = cv2.imread("thresImg.JPG")
rectImg = cv2.rectangle(tImg, (20,20), (500,500), (0,0,255), 2)
textImg = cv2.putText(tImg, "Hello world!", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
cv2.imwrite("thresImg.JPG",tImg)