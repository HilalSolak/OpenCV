import cv2
import numpy as np
#basic functions ,resizing and cropping
img1=cv2.imread("resources/ben.jpg")
img=cv2.resize(img1,(768,1024))
cv2.imshow("imgg ",img)
kernel= np.ones((5,5),np.uint8)
imgBlur=cv2.GaussianBlur(img,(7,7),0)
imgCanny=cv2.Canny(img,100,100)
imgDialation=cv2.dilate(imgCanny,kernel,iterations=1) #iterations=beyazpiksel kalınlığı
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
imgCropped=img[0:200,200:500]
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.imshow("cropped",imgCropped)
cv2.waitKey(0)