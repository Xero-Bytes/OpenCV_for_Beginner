#Cropping image using slicing
import cv2
image = cv2.imread("cat1.jpg")
if image is not None:
    cropped=image[100:400,150:350]
    cv2.imshow("Orignal",image)
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")