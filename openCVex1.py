import cv2
img = cv2.imread('sample1.JPG')
# cv2.imshow("My Logo", img)
# cv2.imwrite("aakashLogo.JPG",img)
# cv2.waitKey(0);
# cv2.destroyAllWindows()

print(img.shape)
print(img.size)
print(img.dtype)

grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#threshold image value decides different aspects of coloring image.
thresImg = cv2.threshold(grayimg,120,255,cv2.THRESH_BINARY)[1]
cv2.imwrite("grayLogo.JPG",grayimg)
cv2.imwrite("thresImg.JPG",thresImg)
# cv2.imshow("Original",img)
# cv2.imshow("GrayImage",grayimg)
cv2.imshow("Threshold Image",thresImg)
cv2.waitKey(0)
cv2.destroyAllWindows()