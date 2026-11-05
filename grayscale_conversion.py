import cv2
image = cv2.imread("python_image.jpg")
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Cat is Gonna to Be BW!",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("grayscale.jpg",gray)
    print("Your GrayScale Cat Image Is Loaded Successfully at OpenCv folder!")
else:
    print("Inage Could Not Find!")    
