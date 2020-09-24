from attributes import ME, AI_ASSISTANT
from voice_system import VoiceSystem
import webbrowser
import random
import json

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def give_command(query):
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
            edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
            webbrowser.get(edge_path).open(url)
        
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)


    elif "play" in query.lower() or "music" in query.lower() or "music on youtube" in query.lower() or "song" in query.lower():
        with open("json/music_list.json") as music_list:
            ml = json.load(music_list)
        random.shuffle(ml['music_list'])
        pick = random.choice(ml['music_list'])

        voice_Sys.speak(f"Ok, playing some music..")
        url = f"www.youtube.com/watch?v={pick}"
        edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
        webbrowser.get(edge_path).open(url)
    
    else:
        return 1