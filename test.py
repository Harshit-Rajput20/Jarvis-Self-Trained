import pyautogui
from Body.speak import speak
import speech_recognition as sr
import os
import pywhatkit
import pyautogui
import time
import webbrowser

def listen():
    r=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source,0,8)
        
    try:
        print("Recognition...")
        query = r.recognize_google(audio,language="en")
        
    except:
        return "" 
    
    query = str(query).lower()
    print(query)
    return query

# Capture the current mouse cursor position
x, y = pyautogui.position()

# Print the coordinates

print(f"X: {x}, Y: {y}")
 


# # Type your message
# pyautogui.typewrite("harshdeep")

# # Press Enter to send the message
# pyautogui.press('enter')


# pyautogui.click(x=3090, y=1027)  # Replace with the actual coordinates of the input box

# # Type your message
# pyautogui.typewrite("bosdike")
 

# # Press Enter to send the message
# pyautogui.press('enter')


# speak('opening youtube')
# webbrowser.open("https://www.youtube.com/")
# time.sleep(5)
# pyautogui.click(x=905, y=177)
# while True:
#     speak("What are you looking for?")
#     video_name = listen().lower()
#     pyautogui.typewrite(video_name)
#     pyautogui.press('enter')    
#     if video_name:
#         break
# while True:
#     speak("Which video do you want to play?")
#     vedio = listen().lower()
    
#     if vedio in ['first', 'second', 'third', 'fourth']:
#         break
    
#     speak("I'm sorry, please specify 'first', 'second', 'third', or 'fourth' for the video.")
    
# if vedio == 'first':
#     speak("Playing first video")
#     pyautogui.click(x=801, y=340)
#     pyautogui.press('enter')
# elif vedio == 'second':
#     speak("Playing second video")
#     pyautogui.click(x=766, y=562)
#     pyautogui.press('enter')
# elif vedio == 'third':
#     speak("Playing third video")
#     pyautogui.click(x=741, y=834)
#     pyautogui.press('enter')
# elif vedio == 'fourth':
#     speak("Playing fourth video")
#     pyautogui.click(x=764, y=1026)
#     pyautogui.press('enter')



# pyautogui.press('fn', 'f4')
    
    
    
 
  


