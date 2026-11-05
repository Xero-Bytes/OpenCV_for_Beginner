#width=center horizantolly
#Height=Center vertically
#image rotation and flipping      
import cv2
image = cv2.imread("python_image.jpg")
if image is None:
    print("Image Not Found!")
else:
    (w,h)=image.shape[:2]
    print("Image Loaded!")
    center=(w//2,h//2)
    m=cv2.getRotationMatrix2D(center,90, 1.0)
    rotation=cv2.warpAffine(image,m,(w,h))  
    cv2.imshow("orignal",image)
    cv2.imshow("rotated90Degree",rotation) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()