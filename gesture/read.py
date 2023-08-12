# Import the required module for text to speech conversion
from gtts import gTTS
  
# This module is imported so that we can play the converted audio
import os
  
mytext = 'ciao marco'
  
language = 'it'
  
myobj = gTTS(text=mytext, lang=language, slow=False)
  
myobj.save("welcome.mp3")
  
os.system("afplay welcome.mp3")
