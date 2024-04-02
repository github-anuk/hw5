import cv2
import numpy as np

img=cv2.imread("eye.png",cv2.IMREAD_COLOR)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_blurred=cv2.blur(gray,(3,3))

#apply hough transformation function

detected_circles = cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20, param1 = 50 ,param2= 30,minRadius=1, maxRadius=40)

#ThE ArT PrOcEsS

#DRaWiNg CiRcLeas ArOuNd CiRcle

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))

    for i in detected_circles[0,:]:
        a,b,r= i [0],i[1] , i[2]
        cv2.circle(img, (a,b),r,(0,225,0),2)
        cv2.circle(img,(a,b),1,(0,0,225),3)
    cv2.imshow("circle",img)
    cv2.waitKey(0)
