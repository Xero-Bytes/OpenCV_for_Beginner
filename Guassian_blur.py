#Filtering image
#Gaussian Blur (To soft an image making smooth reduce sharpness ,remove noise)(kernal_size always odd(3,3)or(5,5))
#blendding =All Values (pixels) sums/average then cahnge the canter value with average value
#Median Blur
#Sharpening Filters
#Raw image to Enhanced image
import cv2
image=cv2.imread("python_image.jpg")
blurred=cv2.GaussianBlur(image,(21,21),3)     #source_image ,kernal(odd_nbr),end nbr is sigma
cv2.imshow("Orignal Image",image)
cv2.imshow("Blurred Image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()