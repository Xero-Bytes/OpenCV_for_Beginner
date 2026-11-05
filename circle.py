#Drawing rectangle on an image
import cv2
image = cv2.imread("cat1.jpg")
if image is not None:
    print("Image load Successfully!")
    cv2.circle(image,(300,300),80,(0,255,0),1)
    cv2.imshow("Circle on Catoo:)",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("OOPS! Where Is Your Image Buddy:)")    