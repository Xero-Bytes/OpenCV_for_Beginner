#Thresholding is a method to  convert image into black & White based on brightness
#up brightness white low dark black
#just take necessary things
#method   --->what kind of Thresholding   usually BinaryThresh     255-white  0-black
#cv2.threshold(image,threshvalue,max_value,method)
#              grayscaleimg ,0-255,255,
import cv2
image=cv2.imread("python_image.jpg",cv2.IMREAD_GRAYSCALE)
ret,thresh_img=cv2.threshold(image,100,255,cv2.THRESH_BINARY)
cv2.imshow("Orignal_Catoo",image)
cv2.imshow("Threshold_Catoo",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#90 - 0 black  (b/c 90<120)
#130-255 white (b/c 130>120)
#180-255 white
#50-0 black