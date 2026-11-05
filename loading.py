import cv2
image = cv2.imread("cat1.jpg")
if image is None:
    print("Error: Image Not Found!")
else:
    print("Image Loaded Successfully!")
cv2.imshow("My Cuttie Catoo :)",image)
cv2.waitKey(5000)
cv2.destroyAllWindows()   
cv2.imwrite("output.jpg",image) 