import speech_recognition as sr
from plyer import notification
import pygame
import time


import gtts
import pygame
import os
import datetime
import subprocess


# this is assistent code for Ubuntu 


def speak(text):
    tts = gtts.gTTS(text,lang="hi")
    tts.save("output.mp3")

    print(f"You: {text}.")

    pygame.mixer.init()

    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    # Clean up the generated audio file
    os.remove("output.mp3")


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=8)  # Set a timeout of 8 seconds for voice input

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
        return ""

    query = query.lower()
    return query

def read_alarm_time():
    try:
        with open("Alarmtext.txt", "rt") as file:
            time_text = file.read()
        return str(time_text)
    except FileNotFoundError:
        return None

def delete_alarm_time():
    with open("Alarmtext.txt", "w"):
        pass
extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt","r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis", "").replace("set an alarm", "").replace(" and ", ":")
    Alarmtime = str(timenow)
    print(Alarmtime)

    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing, sir")
            
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            
            # Load and play the music file
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(80) 
            pygame.mixer.music.load('music.mp3')  
            pygame.mixer.music.play()
            pygame.time.wait(10000)  # 4000 milliseconds = 4 seconds

        # Stop the sound
            pygame.mixer.music.stop()

            
            
ring(time)