from gtts import gTTS
import os
from playsound import playsound

# path of the text file
text_file = "text.txt"

# open the text file and read its contents
with open(text_file, "r") as f:
    text = f.read()

# create the gTTS object
tts = gTTS(text, lang='en')

#check if there is some other file with same name present or not, if present delete it
file_name = "audio4.mp3"
if os.path.exists(file_name):
    os.remove(file_name)

# save the mp3 file
tts.save(file_name)

#play the audio
playsound(file_name)
