import os
from PIL import Image
from gtts import gTTS
import mediapipe as mp
from matplotlib import pyplot as plt
from mediapipe.framework.formats import landmark_pb2

def prediction(recognizer, image):
    im = Image.fromarray(image)
    im.save(os.getcwd()+"/your_file.jpeg")
    image = mp.Image.create_from_file("your_file.jpeg")
    recognition_result = recognizer.recognize(image)
    #Parte da fixare
    try:
        print(recognition_result.gestures[0][0].category_name)
        return recognition_result.gestures[0][0].category_name
    except:
        return

def read(gesture):
    mytext = ""

    if(gesture == "Open_Palm"):
        mytext = 'Alexa spegni computer'
    elif(gesture == "Thumb_Up"):
        mytext = "Alexa spegni il display"
    elif(gesture == "None"):
        mytext = "Nessuna rilevazione"
    
    if not mytext== "":
        language = 'it'
        
        myobj = gTTS(text=mytext, lang=language, slow=False)
        
        myobj.save("speech.mp3")
        
        os.system("afplay speech.mp3")