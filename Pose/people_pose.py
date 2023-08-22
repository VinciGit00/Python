import cv2
import numpy as np
import mediapipe as mp

# Initialize Mediapipe components
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def main():

    first_image = True
    count = 0
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    cv2.resizeWindow("Resized_Window", 300, 700)

    # Initialize Mediapipe Pose model
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if first_image:
                count = count + 1
                if count == 10:
                    array = np.asarray(frame)
                    left, rigth, top, bottom = int(0.975*array.shape[0]) , int(1.25*array.shape[0]), int(0.05*array.shape[1]), 0

                    cropped_array = array[left:rigth, bottom:top]

                    # Convert the array to grayscale
                    gray_array = cv2.cvtColor(cropped_array, cv2.COLOR_BGR2GRAY)

                    # Calculate the average intensity (luminance)
                    luminance = np.mean(gray_array)
                    print("Luminance:", luminance)

                    if(luminance < 127):
                        color = (0, 0, 0)
                    else: 
                        color = (255, 255, 255)

                    first_image = False

            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)

            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with the Pose model
            results = pose.process(rgb_frame)

            if results.pose_landmarks and count >= 10:
                # Draw pose landmarks on the frame with red circles and black lines
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=5, circle_radius=5),
                                          connection_drawing_spec=mp_drawing.DrawingSpec(color=color, thickness=5))

            # Display the resulting frame
            cv2.imshow('Pose Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
