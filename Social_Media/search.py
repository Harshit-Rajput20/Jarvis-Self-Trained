


from Body.speak import speak
 
import speech_recognition as sr
import os
import pywhatkit
import pyautogui
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
 
import datetime
import cv2




def searchGoogle(query):
    if "search" in query:
        import wikipedia as googleScrap
       
        query = query.replace("search","")
        query = query.replace("google","")
        speak("This is what I found on google")
        print(query)

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")
    
   
    
                
    