import cv2
image = cv2.imread("cat1.jpg")
Show = input("Do You Want to Load It? ")
if image is not None:
    if Show.lower() == "yes":
        cv2.imshow("Hi Im There!", image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
    else:
        Save = input("Do You Want to Save It? ")
        if Save.lower() == "yes":
            cv2.imwrite("User_want_save.jpg", image)
            print("Your Cat Image Is Saved Successfully!")
        else:
            print("Image Not Saved!")
else:
    print("Image Not Loaded!")