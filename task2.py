
import cv2

# Take image location from user
image_path = input("Give me your image file location: ")

# Load image
image = cv2.imread(image_path)

# Check whether image is loaded
if image is None:
    print("Oops! Image file not found.")

else:
    print("Image Loaded Successfully!")

    while True:
        print("\n========== MENU ==========")
        print("1. Add Line")
        print("2. Add Circle")
        print("3. Add Rectangle")
        print("4. Add Text")
        print("5. Exit")

        choice = input("Choose an option: ")

        # Add Line
        if choice == "1":
            pt1 = (50, 200)
            pt2 = (650, 150)
            color = (255, 0, 0)
            thickness = 8

            cv2.line(
                image, pt1, pt2, color, thickness
            )

        # Add Circle
        elif choice == "2":
            center = (300, 300)
            radius = 80
            color = (0, 255, 0)
            thickness = 3

            cv2.circle(
                image, center, radius, color, thickness
            )

        # Add Rectangle
        elif choice == "3":
            pt1 = (200, 250)
            pt2 = (400, 450)
            color = (255, 0, 0)
            thickness = 8

            cv2.rectangle(
                image, pt1, pt2, color, thickness
            )

        # Add Text
        elif choice == "4":
            text = "Hii! I am a cute Cat!"
            position = (200, 350)
            font = cv2.FONT_HERSHEY_COMPLEX
            font_scale = 1.2
            color = (255, 0, 255)
            thickness = 2

            cv2.putText(
                image,
                text,
                position,
                font,
                font_scale,
                color,
                thickness
            )

        # Exit
        elif choice == "5":
            print("Program Closed!")
            break

        else:
            print("Invalid Option! Try Again.")
            continue

        # Display image
        cv2.imshow("My Drawing", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Ask user whether to save
        save = input("Do you want to save it? (yes/no): ")

        if save.lower() == "yes":
            filename = input(
                "Enter output filename (e.g. result.jpg): "
            )

            success = cv2.imwrite(filename, image)

            if success:
                print("Image Saved Successfully!")
            else:
                print("Image Could Not Be Saved!")

        else:
            print("Image Not Saved!")
