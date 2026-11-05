#Drawing Line on an image
import cv2
image = cv2.imread("cat1.jpg")
if image is not None:
    print("Image load Successfully!")
    ptd1=(50,300)   #x,y  x descibe how much pixels right and then y describe how much pixels down
    ptd2=(700,150)  #x,y
    color=(255,0,0)
    thickness=8
    cv2.line(image,ptd1,ptd2,thickness)
    cv2.imshow("Drawing Catoo:)",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("OOPS! Where Is Your Image Buddy:)")    