#Functions
import os
import math
import mediapipe as mp
from PIL import Image
from matplotlib import pyplot as plt
from mediapipe.framework.formats import landmark_pb2

def prediction(recognizer, image):
    im = Image.fromarray(image)
    im.save(os.getcwd()+"/your_file.jpeg")
    image = mp.Image.create_from_file("your_file.jpeg")
    recognition_result = recognizer.recognize(image)
    print(recognition_result)
    return recognition_result.gestures
    #return recognition_result.gestures[0][0].category_name
