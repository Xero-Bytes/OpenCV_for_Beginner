#contours    curve which combine contaginous point .of same colur and intensity
#cv2.findscontours(image(black and white),mode(retrival mode(tree or external)),method(approximation(chain)))
#return list of all points detected in an shape                    contours
#informations of contours level  (parent to child)    relationship between the conteurs which returns              hierracy
#Mode---How many contours returns and what kinds of contours return
#retrivel-external   ---only return outer square
#retrivel-tree       --shape and inner square complete hierarcy
#retrivel list         return all but not hierarcy 
#method==it tell how much detail to return for each contour
import cv2
img=cv2.imread("circle.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
#Find Contours
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#DrawContours
#ConterIndex  it tell which shape draw? if we write 0 it tell just 1st shape draw 1 tell 2nd shape -1 tell all shape in list draw
cv2.drawContours(img,contours,-1,(0,255,0),3)
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()