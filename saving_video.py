#avi   audio video interleaue
#codec    compression format
#fps frame per second
#frame size  width height
import cv2
camera=cv2.VideoCapture(0)
frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_Height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec=cv2.VideoWriter_fourcc(*'XVID')
recorded=cv2.VideoWriter("my_video.avi",codec,20,(frame_width,frame_Height))
while True:
    success,image=camera.read()
    if not success:
        break
    recorded.write(image)
    cv2.imshow("Recording Live!",image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
            print("Quitting...")
            break
camera.release()   #it close camera
recorded.release()
cv2.destroyAllWindows()
