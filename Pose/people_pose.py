import cv2
import mediapipe as mp

# Initialize Mediapipe components
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)

    # Initialize Mediapipe Pose model
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)

            # Convert the BGR image to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame with the Pose model
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
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
