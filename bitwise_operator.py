"""
1-cv2.bitwise_and(img1,img2) like just face area cut in an image
2-cv2.bitwise_or(img1,img2)   murge multiple effects in one image
3-cv2.bitwise_not(img1)       white to black and black to white
"""
import cv2
import numpy as np
img1=np.zeros((300,300),dtype="uint8")
img2=np.zeros((300,300),dtype="uint8")
cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2,(100,100),(250,250),255,-1)
bitwise_and=cv2.bitwise_and(img1,img2)
bitwise_or=cv2.bitwise_or(img1,img2)
bitwise_not=cv2.bitwise_not(img1)
cv2.imshow("Circle",img1)
cv2.imshow("Rectangle",img2)
cv2.imshow("And",bitwise_and)
cv2.imshow("Or",bitwise_or)
cv2.imshow("Not",bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
