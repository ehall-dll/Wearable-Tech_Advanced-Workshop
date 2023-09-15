''' 

    This is a translated/broken down version of the Text-To-Speech Code.

'''

# Here we are telling Python that we need to include some 'libraries' these are like tools in our toolkit that python can use
# They are not carried by default as, it would be like taking everything from your home with you every day! - You take what you need.
import os
from gtts import gTTS
import playsound  # To play the saved mp3 file
import tempfile  # To create a temporary file

# This line is the equivilant of typing into the terminal 'Clear', this just clears the screen for us. The OS & System are just telling
# Python that it needs to talk directly to the Operating System (OS) and use some System Commands.
os.system('clear')

# Here we are creating a mini program inside of our code that we can use over an over again to seak text, the 'def' stands for define,
# as we are defining the name of our program (or function). Here we name it 'speak' but this could be anything. 
# Lastly we have an required, here named 'text', again this could be named anything, but we've called it 'text' and it will be referred as that,
# all the way through our function (And ONLY inside of our function, we would have to redefine it outside of our function, just like words are different country to country).
# This required 'text' will be input later when the function is run, as here we are just defining it, like a dictionary.

def speak(text):
    # Here we are creating a variable called tts (text to speach), with some requirements for the program, (this is not something we know already, but the documentation for the toolkit/library we imported tells us!)
    # In this case we are the text to be spoken is equal to our input named 'text' if we has named it input it would read 'text = input' instead of 'text = text'
    # Lastly we are saying the language to be used for our speech is 'English' or 'en' for short! - again the documentation tells us what to put here.
    tts = gTTS(text=text, lang='en')
    # Here we are creating a temporary file to save the audio to called 'temp_file' but we could call this anything we like such as 'The File', this is a bit more technical, but we could just have it save the file,
    # but the more we run the code the more files we would have and soon we could become horders!
    temp_file = tempfile.NamedTemporaryFile(delete=True)
    # Here we are looking at our variable we created earlier called 'tts' on line 28. Again this is not soemthing we are expected to know. instead the documentation tells us we can append a '.save' with the attriubutes such as the file name and audio type.
    # When we use '.'s it signifies a 'Class' this is a bit more technical, but in this case you can imagine it like a premade function.
    tts.save(temp_file.name + '.mp3')
    # Same again here, this time we are playing the sound using our toolkit/library called 'playsound' that we imported on line 11. Telling the tool what file we want to open and the file format.
    playsound.playsound(temp_file.name + '.mp3')


# Ask the user for their name
# Here we are not outside of the function and are just creating a variable for input, this could also be seen once filled out as "user_name = "Elliott"
# "What is your name", is just text that will be displayed to the user, and is a nice tool we can use with the input() function.
user_name = input("What is your name? ")

# Saving Response as a variable (String Format)
# Here the response is saved to a variable called 'responce' which if we imagined this was filled out would say: [ response = ("Hello, " + "Elliott" + "!") ] or for short [ response = ("Hello, Elliott!") ]
response = ("Hello, " + user_name + "!")

# Say hello to the user
# this now prints or displays the contents of our variable, in our instance response equals: "Hello, Elliott!"
print(response)

# Speak the response
# This is now where we run our function speak witht the responce placed in it to be spoken. This could be better imagined as:
speak(response) # speak("Hello, Elliott!")
# Both of which would work, however, the one with 'response' would adapt to whatever the user had input themselves, and not just my name!

# You can now look back at the function and in your mind replace the variable 'text' with "Hello, Elliott!" such as:

# tts = gTTS(text="Hello, Elliott!"", lang='en')

# instead of

# tts = gTTS(text=text, lang='en')