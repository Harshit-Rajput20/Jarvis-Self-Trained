# import requests
# from bs4 import BeautifulSoup

# search = "temperature in delhi"
# url = f"https://www.google.com/search?q={search}"
# r = requests.get(url)
# data = BeautifulSoup(r.text, "html.parser")

# # The class name might change, so it's good to inspect the HTML source and adjust accordingly
# temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
# print(temp)


# import pyautogui

# import speech_recognition
# import pyttsx3
# import pywhatkit
# import wikipedia
# import webbrowser




# this is assistent code for Ubuntu 
import gtts
import pygame
import os
import time
import requests

class NoInternetConnectionError(Exception):
    pass

def speak(text):
    try:
        while True:
            check_internet_connection()

            # Generate audio from text using gTTS
            tts = gtts.gTTS(text, lang="hi")
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

            # Wait for 1 second before checking internet connection again
            time.sleep(1)

    except KeyboardInterrupt:
        # Handle keyboard interrupt (e.g., when you stop the program)
        print("Program terminated.")

def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        response.raise_for_status()
        print("Internet connection is available.")
    except requests.ConnectionError:
        raise NoInternetConnectionError("Internet connection error: Could not establish a connection.")
    except requests.Timeout:
        raise NoInternetConnectionError("Internet connection error: Request timed out.")
    except requests.RequestException as e:
        raise NoInternetConnectionError(f"Internet connection error: {e}")

# Call the speak function with a sample text
speak("Hello, how are you?")
