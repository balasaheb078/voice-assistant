import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
from time import sleep
import os

recognizer  = sr.Recognizer()

engine = pyttsx3.init()
newsapi = "ac0056541f47443f9c6fa3388684bf28"

def speakOld(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running to allow the music to play
    while pygame.mixer.music.get_busy():
        sleep(1)
    # Unload the MP3 file
    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def processCommand(c):
     if  "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open facebook" in c.lower():
          webbrowser.open("https://facebook.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif "open linkdin" in c.lower():
          webbrowser.open("https://linkedin.com")
     elif "open mispack" in c.lower():
          webbrowser.open("https://mispack.in")
     elif c.lower().startswith("play"):
          song = c.lower().split(" ")[1]
          link=musicLibrary.music[song]
          webbrowser.open(link)
     elif "news" in c.lower():
          r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
            # Check if the request was successful
          if r.status_code == 200:
                
                # Parse the JSON response
                data = r.json()

                # Extract the headlines
                headlines = [article['title'] for article in data['articles']]

                # Print the headlines
                for idx, headline in enumerate(headlines, start=1):
                    speak(f"{idx}. {headline}")
          else:
               speak("Failed to fetch the headlines")
     
if __name__ =="__main__":
    speak("Initializing friend....")
# obtain audio from the microphone
    while True:
        # Listen for the wake word friend
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                
                print("Listening...")
                audio = r.listen(source, timeout=3,phrase_time_limit=1)    

            word = r.recognize_google(audio)
            if(word.lower()=="hello"):
                speak("Yaa")
                    #  listen  for command
                with sr.Microphone() as source:
                     print("Friend active...")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)
                     speak("sure")
                     processCommand(command)
                                                                                             
       
        except Exception as e:
                print("Error; {0}".format(e))    