from attributes import ME, AI_ASSISTANT
import webbrowser
import random
import json
from voice_system import VoiceSystem

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def give_command(query):
    if "terminate the program" == query.lower() or "goodbye" == query.lower() or "terminate" == query.lower() or "no" == query.lower() or "nope" == query.lower() or "nothing" == query.lower() or "terminate" in query.lower():
        voice_Sys.speak(f"Ok, goodbye {ME}")
        exit()

    elif 'open youtube' in query.lower():
        voice_Sys.speak(f"Ok, openning youtube..")
        url = "www.youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif ('open google' or 'open chrome') in query.lower():
        voice_Sys.speak(f"Ok, openning google..")
        url = "www.google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    elif ('open fb' or 'open facebook') in query.lower():
        voice_Sys.speak(f"Ok, openning facebook..")
        url = "www.facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    #phb
    elif "open p******" in query.lower():
        voice_Sys.speak(f"Ok, openning \u0070\u006F\u0072\u006E\u0068\u0075\u0062..")
        url = "www.\u0070\u006F\u0072\u006E\u0068\u0075\u0062.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)

    elif "play" in query.lower() or "music" in query.lower() or "music on youtube" in query.lower():
        with open("json/music_list.json") as ml:
            music_list = json.load(ml)

        random.shuffle(music_list)
        voice_Sys.speak(f"Ok, playing some music..")
        url = f"www.youtube.com/watch?v={music_list[1]}"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    
    else:
        return 1