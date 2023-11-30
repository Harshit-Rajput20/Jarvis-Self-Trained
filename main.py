# from Body.listen import listen
# from Body.speak import speak


 
# def mainx():    

#     Tester()
#     speak("Welcome Sir")

 
# mainx() 

 
# def wakeUp():
#     queery = listen().lower()

    
#     if "wake up" in queery:
#         pass
    
#     else:
#         pass
import pygame
    
pygame.init()

# Initialize pygame mixer with desired parameters
pygame.mixer.init()


def listen():
    try:
        print("listening.....")
        r=sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio =r.listen(source,0,8)
            
            
        try:
            print("Recognition...")
        
            query = r.recognize_google(audio,language="en")
            print("bakchodi det4ecter") 
        except:
            return "" 
        
        query = str(query).lower()
        
        print(query)
        
        return query
    except:
        return ""

# def wakeUp():

waked = False


def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")
        


print("test -1")
while True:    
    try:
            
        from Features.clap import Tester

        import cv2
        import pyautogui
        import datetime
        import requests    

        import speech_recognition as sr
        import os
        from jarvis import mainExe
        from Body.speak import speak

    except:
        continue
    try:
        # Try making a simple GET request to a reliable server
        print("Test0")
        response = requests.get("http://www.google.com", timeout=5)
        print("Test1")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        print("Test2")
        
        print("Internet connection is available.")
        
        
        if(response.ok):
            print("connnected")
        else:
            print("not connected")


        while not waked:
            
            

            
                
            query = listen().lower()
            # query = input("enter wake up") 
            
            
            if "wake up" in query or "hello" in query:
                
                try :                       
                    pygame.mixer.music.load('computer-processing-sound-effect-01-122131.mp3')  
                    pygame.mixer.music.play()
                    pygame.time.wait(2000)  # 4000 milliseconds = 4 seconds
                    # Stop the sound
                    pygame.mixer.music.stop()
                except:
                    pass
                speak("authentication checking")
                
            

                import cv2

                recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
                recognizer.read('trainer/trainer.yml')   #load trained model
                cascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

                font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


                id = 2 #number of persons you want to Recognize


                names = ['','harshit']  #names, leave first empty bcz counter starts from 0


                cam = cv2.VideoCapture(0) #cv2.CAP_DSHOW to remove warning
                cam.set(3, 640) # set video FrameWidht
                cam.set(4, 480) # set video FrameHeight

        # Define min window size to be recognized as a face
                minW = 0.1*cam.get(3)
                minH = 0.1*cam.get(4)

        # flag = True
                mainFlag = True
                while mainFlag:
                    
                    flag = 0 

                    ret, img =cam.read() #read the frames using the above created object
                    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

                    faces = faceCascade.detectMultiScale( 
                        converted_image,
                        scaleFactor = 1.2,
                        minNeighbors = 5,
                        minSize = (int(minW), int(minH)),
                    )

                    for(x,y,w,h) in faces:

                        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

                        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

                # Check if accuracy is less them 100 ==> "0" is perfect match 
                        if (accuracy < 100):
                            id = names[id]
                            accuracy = "  {0}%".format(round(100 - accuracy))
                            flag = 1
                            

                        else:
                            id = "unknown"
                            accuracy = "  {0}%".format(round(100 - accuracy))
                
                        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
                    cv2.imshow('camera',img) 

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    if flag == 1:
                        
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                        pyautogui.press('q')
                        cam.release()
                        cv2.destroyAllWindows()
                        speak("verification successful")
                        # greetMe()
                        mainExe()
                        print("After Main exe")
                        
                        mainFlag=False
                        waked= False
                    

        
                print("Thanks for using this program, have a good day.")
                print("MainFlag" , mainFlag)
                            

            
                
                
            
            
            
            else:
                print("")
                print("AI : Not started")
                print("")
                pass
            
    except requests.RequestException as e:
        # speak("internetconnectio error")
        print("some error ")

        print("Internet connection error "+e) 
        
print("Breaked")