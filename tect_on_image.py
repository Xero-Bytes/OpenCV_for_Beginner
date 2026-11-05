#Drawing rectangle on an image
import cv2
image = cv2.imread("python_image.jpg")
if image is not None:
    print("Image load Successfully!")
    cv2.putText(image,"Hii! I'm A cuttie Cattoo!",(200,350),cv2.FONT_HERSHEY_COMPLEX,1.2,(255,0,255),2)
    cv2.imshow("Label Catoo:)",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("OOPS! Where Is Your Image Buddy:)")    