''' 

    This is a simple Python program to greet the user 

    please run the following Prior:
    
    'pip3 install gtts'
    'pip3 install playsound'
    
'''

import os
from gtts import gTTS
import playsound  # To play the saved mp3 file
import tempfile  # To create a temporary file

os.system('clear')

# Function to speak text
def speak(text):
    tts = gTTS(text=text, lang='en')
    temp_file = tempfile.NamedTemporaryFile(delete=True)
    tts.save(temp_file.name + '.mp3')
    playsound.playsound(temp_file.name + '.mp3')

# This is a simple Python program to greet the user

# Ask the user for their name
user_name = input("What is your name? ")

# Saving Response as a variable (String Format)
response = ("Hello, " + user_name + "!")

# Say hello to the user
print(response)

# Speak the response
speak(response)