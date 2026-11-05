import cv2
image = cv2.imread("cat1.jpg")
if image is not None:
    h,w,c=image.shape
    print(f"Image Loaded:\nHeight:{h}\nWidth:{w}\nChannel:{c}")
else:
    print("Could not found image!")    