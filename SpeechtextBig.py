# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment

r = sr.Recognizer()
filename = "1272-141231-0000.flac"

def strip_extension(filename):
    # Remove extension of the filename
    name, extension = os.path.splitext(filename)
    return name


def transcribe_audio(path):
    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    return text


# a function that splits the audio file into fixed interval chunks
# and applies speech recognition
def get_large_audio_transcription_fixed_interval(path, minutes=5):
    """Splitting the large audio file into fixed interval chunks
    and apply speech recognition on each of these chunks"""
    # open the audio file using pydub
    sound = AudioSegment.from_file(path)  
    # split the audio file into chunks
    chunk_length_ms = int(1000 * 60 * minutes) # convert to milliseconds
    chunks = [sound[i:i + chunk_length_ms] for i in range(0, len(sound), chunk_length_ms)]
    folder_name = "Audio-Files"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        try:
            text = transcribe_audio(chunk_filename)
        except sr.UnknownValueError as e:
            print("Error:", str(e))
        else:
            text = f"{text.capitalize()}. "
            whole_text += text
        #Cleaning up the files created from the Chucks
        try:
            os.remove(chunk_filename)
        except OSError as e:
            print(f"Error: {chunk_filename} : {e.strerror}")

    # return the text for all chunks detected
    return whole_text

txt_name = strip_extension(filename) +'.txt'
text = get_large_audio_transcription_fixed_interval(filename)

# Writting all the text extracted to a file
with open(txt_name, 'w') as f:
    f.write(text)

