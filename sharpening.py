#Sharpening Filters   it highlight the edges and boost the contast between pixels
#keranl is basically moving pixels by pixels on an image
#5 mean we boost center with five and subtract with neighbour by -1 and 0 mean ignore corner in image
#through this center become brighter and sharp and corner remain same or blur
import cv2
import numpy as np
image=cv2.imread("python_image.jpg")
shrapeKernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharp=cv2.filter2D(image,-1,shrapeKernel)
cv2.imshow("Orignal Image",image)
cv2.imshow("clean Image",sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()