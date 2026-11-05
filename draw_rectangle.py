#Drawing rectangle on an image
import cv2
image = cv2.imread("cat1.jpg")
if image is not None:
    print("Image load Successfully!")
    ptd1=(300,300)   #Top Left Corner
    ptd2=(200,250)  #Bottom Right Corner
    color=(255,0,0)
    thickness=8
    cv2.rectangle(image,ptd1,ptd2,thickness)
    cv2.imshow("Drawing Catoo:)",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("OOPS! Where Is Your Image Buddy:)")    