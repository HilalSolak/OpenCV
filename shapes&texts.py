import cv2
import numpy as np
img= np.zeros((512,512,3),np.uint8)
#print(img)
#img[:]=255,0,0  #img 'nin tamamını mavi yapmak
# img[200:300,0:100]=255,0,0   img'nin belli kısmını mavi yapmak y değerinin 200den 300e
# xin 0'ından 100. birimine

# ---- how to create line----
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)
cv2.putText(img," OPENCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
cv2.imshow("image",img)
cv2.waitKey(0)