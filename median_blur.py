#Median Blur
#blurred=cv2.MedianBlur(image,Kernal_size)
#we take middle value of neighbours pixels     remove random black and white dots
import cv2
image=cv2.imread("python_image.jpg")
blurred=cv2.medianBlur(image,11)
cv2.imshow("Orignal Image",image)
cv2.imshow("clean Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()