# import the opencv library
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from functions import *

def videocapture(flag_frame):
	base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
	options = vision.GestureRecognizerOptions(base_options=base_options)
	recognizer = vision.GestureRecognizer.create_from_options(options)
	
	vid = cv2.VideoCapture(0)

	while(True):
		
		ret, frame = vid.read()
		
		res = prediction(recognizer, frame)
		read(res)
		if flag_frame:
			cv2.imshow('frame', frame)

			
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

	# After the loop release the cap object
	vid.release()
	# Destroy all the windows
	cv2.destroyAllWindows()

videocapture(False)