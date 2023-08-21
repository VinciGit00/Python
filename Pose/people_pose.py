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
                    print(array.shape)
                    left, rigth, top, bottom = 0.95*array.shape[0] , 1.05*array.shape[0], 0.25*array.shape[1], 0
                    cropped_image = array[left:rigth, bottom:top]

                    pixel_values = np.arange(256)

                    # Map the pixel values in cropped_image to their corresponding quantities in pixel_values
                    mapped_array = pixel_values[cropped_image]
                    #TODO: VADO AVANTI DA QUI IN POI
                    #Qui devo cambiare il colore

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
                                          connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=5))

            # Display the resulting frame
            cv2.imshow('Pose Detection', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
