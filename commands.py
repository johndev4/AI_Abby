from voice_system import VoiceSystem
import webbrowser
import random
from os import path

def give_command(attr, query):
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)

    if "open " in query.lower():
        if 'open youtube' in query.lower():
            voice_Sys.speak(f"Ok, openning youtube..")
            url = "www.youtube.com"
            
        elif ('open google' or 'open chrome') in query.lower():
            voice_Sys.speak(f"Ok, openning google..")
            url = "www.google.com"

        elif "open facebook" in query.lower() or "open fb" in query.lower():
            voice_Sys.speak(f"Ok, openning facebook..")
            url = "www.facebook.com"

        elif "open instagram" in query.lower():
            voice_Sys.speak(f"Ok, openning instagram..")
            url = "www.instagram.com"

        elif "open twitter" in query.lower():
            voice_Sys.speak(f"Ok, openning twitter..")
            url = "www.twitter.com"
        
        #nsfw here
        elif "open p******" in query.lower():
            voice_Sys.speak(f"Ok, openning \u0070\u006F\u0072\u006E\u0068\u0075\u0062..")
            url = "www.\u0070\u006F\u0072\u006E\u0068\u0075\u0062.com"

    elif "play" in query.lower() or "music" in query.lower() or "music on youtube" in query.lower() or "song" in query.lower():
        random.shuffle(attr.music_list)
        pick = random.choice(attr.music_list)

        voice_Sys.speak(f"Ok, playing some music..")
        url = f"www.youtube.com/watch?v={pick}"
    
    else:
        return 1
    
    __browse__(url)

def __browse__(url):
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    ie_path = "C:/Program Files/Internet Explorer/iexplore.exe"
    firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe"

    if path.exists(edge_path):
        webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open(url)
    elif path.exists(chrome_path):
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
    elif path.exists(firefox_path):
        webbrowser.get("C:/Program Files/Mozilla Firefox/firefox.exe %s").open(url)
    elif path.exists(ie_path):
        webbrowser.get("C:/Program Files/Internet Explorer/iexplore.exe %s").open(url)