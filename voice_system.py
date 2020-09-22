import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio

class VoiceSystem:
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def __init__(self, AI_ASSISTANT, ME):
        self.AI_ASSISTANT = AI_ASSISTANT
        self.ME = ME

    def speak(self, text):
        print(f"{self.AI_ASSISTANT}: {text}")
        VoiceSystem.engine.say(text)
        VoiceSystem.engine.runAndWait()

    def greet(self, ME):
        hour = int(datetime.datetime.now().hour)
        print(hour)

        if hour>=0 and hour<12:
            self.speak(f"Good morning {ME}, it's nice to meet you")   
        elif hour>=12 and hour<18:
            self.speak(f"Good afternoon {ME}, it's nice to meet you")
        else:
            self.speak(f"Good evening {ME}, it's nice to meet you")

    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source)
        
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-us')
            if self.ME == "":
                print(f"You said: {query}\n")
            else:
                print(f"{self.ME} said: {query}\n")
                
        except Exception:
            query = ""
            self.speak("Sorry, I can't here you.")
            
        return query