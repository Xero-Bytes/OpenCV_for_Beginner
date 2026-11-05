#epsilon==0.01*cv2.arclength(contour,True)
#0.01 turning parameter epsilon
"""
Shape                    arclength                   epsilon
                                                     0.01(x)
small triangle           200pixels                   0.01*200=2pixels
large Square             800pixels                   0.01*800=8pixels
Big Circle               1200Pixels                  0.01*1200=12pixels

"""
import cv2
img=cv2.imread("circle.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(0,255,0),3)
for contour in contours:
    approx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    corners=len(approx)
    if corners==3:
        shape_name="Triangle"
    elif corners==4:
            shape_name="Rectangle"
    elif corners==5:
            shape_name="pentagon"            
    elif corners>5:
            shape_name="Square"
    else:
          shape_name="Unknown"

    cv2.drawContours(img,[approx],0,(0,255,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1]-10
    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,0,0))              
cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()