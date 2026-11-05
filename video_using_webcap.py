#Frame=image
#video=many frame
#Frame-by-Frame Processing: Detect frame in video
#if u pass video from computer webcame u enter 0 and in case of external webcame u have to enter 1
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret ,frame=cap.read()#ret=true,false frame=image
    if not ret:
        print("Could not read frame!")
        break
    cv2.imshow("Webcam Feed!",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        print("Quitting...")
        break
cap.release()   #it close camera
cv2.destroyAllWindows()
cv2.VideoWriter()