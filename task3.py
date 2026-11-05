#user perspective asked user do you want to recoed read see file make it with user perspective

import cv2
import os

# User perspective: Interactive Webcam Recorder

print("\n===== WEBCAM VIDEO SYSTEM =====")
print("1. Live Webcam Preview")
print("2. Record Video")
print("3. Watch Saved Video")
print("4. Exit")

choice = input("What do you want to do? ")

# -------------------------------
# OPTION 1: LIVE WEBCAM PREVIEW
# -------------------------------

if choice == "1":

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Webcam could not be opened!")

    else:
        print("Webcam Started!")
        print("Press Q to close webcam.")

        while True:
            ret, frame = cap.read()

            if not ret:
                print("Frame could not be captured!")
                break

            cv2.imshow("Live Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


# -------------------------------
# OPTION 2: RECORD VIDEO
# -------------------------------

elif choice == "2":

    record = input(
        "Do you want to record a video? (yes/no): "
    )

    if record.lower() == "yes":

        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Webcam could not be opened!")

        else:

            filename = input(
                "Enter video filename (example: my_video.mp4): "
            )

            if not filename.lower().endswith(".mp4"):
                filename += ".mp4"

            filter_choice = input(
                "Choose filter: 1. Normal  2. Grayscale  3. Blur: "
            )

            # Webcam properties
            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = 20.0

            # Create video writer
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")

            out = cv2.VideoWriter(
                filename,
                fourcc,
                fps,
                (width, height)
            )

            print("Recording Started!")
            print("Press Q to stop recording.")

            while True:

                ret, frame = cap.read()

                if not ret:
                    print("Frame could not be captured!")
                    break

                # Apply selected filter
                if filter_choice == "2":

                    processed_frame = cv2.cvtColor(
                        frame,
                        cv2.COLOR_BGR2GRAY
                    )

                    # Convert grayscale to 3 channels
                    processed_frame = cv2.cvtColor(
                        processed_frame,
                        cv2.COLOR_GRAY2BGR
                    )

                elif filter_choice == "3":

                    processed_frame = cv2.GaussianBlur(
                        frame,
                        (15, 15),
                        0
                    )

                else:
                    processed_frame = frame

                # Save each processed frame
                out.write(processed_frame)

                # Display live video
                cv2.imshow(
                    "Recording Video",
                    processed_frame
                )

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

            # Release resources
            cap.release()
            out.release()
            cv2.destroyAllWindows()

            print("Recording Finished!")

            if os.path.exists(filename):
                print("Video Saved Successfully:", filename)

    else:
        print("Recording Cancelled!")


# -------------------------------
# OPTION 3: WATCH SAVED VIDEO
# -------------------------------

elif choice == "3":

    video_path = input(
        "Enter your saved video file location: "
    )

    if os.path.exists(video_path):

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print("Video could not be opened!")

        else:

            print("Video Playing!")
            print("Press Q to stop video.")

            while True:

                ret, frame = cap.read()

                if not ret:
                    print("Video Finished!")
                    break

                cv2.imshow("Your Saved Video", frame)

                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()

    else:
        print("Video File Not Found!")


# -------------------------------
# OPTION 4: EXIT
# -------------------------------

elif choice == "4":

    print("Thank you for using Webcam System!")


else:

    print("Invalid Option! Please Try Again.")
