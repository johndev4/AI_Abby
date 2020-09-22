from constant_variables import ME, CREATOR, AI_ASSISTANT
import wikipedia
from voice_system import VoiceSystem

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def explore(query):

    if "who is your creator" in query.lower():
        voice_Sys.speak(f"{CREATOR} is my creator. He built me with python language on September 19, 2020")

    elif f"who is {CREATOR}".lower() in query.lower():
        voice_Sys.speak(f"{CREATOR} is the one who built me. He built me with python language on September 19, 2020")
    
    elif "search " in query.lower():
        query = query.replace("search ","")
        voice_Sys.speak(f"Searching {query} in wikipedia...")
        results = wikipedia.summary(query,sentences=2)
        voice_Sys.speak(results)
    
    else:
        return 1