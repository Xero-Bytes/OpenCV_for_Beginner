import cv2
image = cv2.imread("cat1.jpg")
if image is None:
    print("Image Not Found!")
else:
    print("Image Loaded!")
    resized=cv2.resize(image,(300,300))
    cv2.imshow("Orignal Image:",image)
    cv2.imshow("Resized Image:",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("rezized_image.jpg",resized)  