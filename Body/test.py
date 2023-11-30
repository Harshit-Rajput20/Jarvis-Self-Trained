import sys
import speech_recognition as sr
from googletrans import Translator
import warnings

# Print the path to the speech_recognition module
print(sr.__file__)

# Suppress ALSA-related warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")

    # Redirect stderr for speech_recognition
    sys.modules['speech_recognition'].__stderr__ = open('/dev/null', 'w')

    # Redirect stderr for googletrans
    sys.modules['googletrans'].__stderr__ = open('/dev/null', 'w')

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recognition...")
        query = r.recognize_google(audio, language="hi")

    except:
        return ""

    query = str(query).lower()
    return query

def translation(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"you: {data}.")
    return data

def connection():
    query = listen()
    data = translation(query)
    return data

# Uncomment the line below to test the listen function
listen()
