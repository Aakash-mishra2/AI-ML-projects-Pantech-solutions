import cv2
import time
import imutils
cam = cv2.VideoCapture(0)
time.sleep(1)

firstFrame=None
area = 500
#area for 

while True:
    _,img = cam.read()
    text = "Normal"
    #resize an image
    img = imutils.resize(img, width=500)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21,21), 0)
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    #comparision with background image, b/w first frame and background image
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    #FIND thresholding of image
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    #dilation to remove holes dots inside image
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    #contours to find neighbourhood pixels so img is connected-how much area is different
    #find area which is different so thus it's moving 
    #contours applied on copy of threshold image as it can't be used again
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #get all contours using imutils
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        #get dimn to draw rectangle around moving object cnts points
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        text = "Moving object detected"
    print(text)
    #outside the for loop so no moving obj detected if no contours
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    cv2.imshow("cameraFeed",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("e"):
        break
cam.release()
cv2.destroyAllWindows()