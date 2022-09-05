import cv2
import numpy as np

img= cv2.imread("resources/cards.jpg")
print(img.shape)
width,height=496,522
pts1=np.float32([[117,229],[297,197],[364,458],[159,501]])
pts2=np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("output", imgOutput)
cv2.waitKey(0)