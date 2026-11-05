#  #flipcode =0  flip vertically  top to bottom  1 horizontally lef to right 
#  -1 both horizontally and vertically

import cv2
image = cv2.imread("cat1.jpg")
if image is None:
    print("Image Not Found!")
else:
    flipped_horizontal=cv2.flip(image,1)
    flipped_Vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)
    cv2.imshow("orignal",image)
    cv2.imshow("Mycat",flipped_horizontal)
    cv2.imshow("Mycat",flipped_Vertical)
    cv2.imshow("Mycat",flipped_both) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()