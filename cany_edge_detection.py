#it draw the outline of the image  where brightness is suddenly changes
#to detect borders
#to seprate objects
#Feature Extraction
#To add sketch effect on an image
#john Canny
#edges=cv2.canny(image,Threshold1,threshold2) 
# T1 lower Boundary to detect weak edges,T2 upper boundary for strong edges
#Threshold   set cutof point for brightness    convert image into black & White based on brightness
#pixel>Threshold   white
#pixel<Threshold   black 
#Yes/No desicion
import cv2
image=cv2.imread("python_image.jpg",cv2.IMREAD_GRAYSCALE)
edges=cv2.Canny(image,50,255)
cv2.imshow("Orignal_Catoo",image)
cv2.imshow("GrayScale_Catoo",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
