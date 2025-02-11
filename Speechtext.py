#pip3 install SpeechRecognition pydub
# Do not forget to install the library before using it
import speech_recognition as sr
import os

def strip_extension(filename):
    # Split the filename into name and extension
    name, extension = os.path.splitext(filename)
    return name

filename = "1272-141231-0000.flac"
# initialize the recognizer
r = sr.Recognizer()
txt_name = strip_extension(filename) +'.txt'

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)

#Create a text file with content from audio 
with open(txt_name, 'w') as f:
    f.write(text)


