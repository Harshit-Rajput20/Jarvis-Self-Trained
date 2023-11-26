import speech_recognition as sr
from plyer import notification
import pygame
import time

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

def timer():
    alarm_time = listen().lower()
    print(f"Setting alarm for: {alarm_time}")

    # Confirm the recognized alarm time with the user
    confirmation = input(f"Confirm the alarm time as '{alarm_time}' (yes/no): ").lower()

    if confirmation == "yes":
        # Continue with setting the alarm
        print("Alarm time confirmed.")
        
        # Path to your alarm sound file (replace with the actual path)
        alarm_sound_file = "/path/to/your/alarm.mp3"

        # Initialize pygame for audio
        pygame.mixer.init()
        current_time = time.strftime("%H:%M")

        if current_time == alarm_time:
            # Display a notification
            notification.notify(
                title="Alarm",
                message="Time to wake up!",
                app_name="My Alarm"
            )

            # Play the alarm tune
            try:
                pygame.mixer.music.load(alarm_sound_file)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"Error: {e}")

    else:
        print("Alarm time not confirmed. Please try again.")

if __name__ == "__main__":
    timer()
