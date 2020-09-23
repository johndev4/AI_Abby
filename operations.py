from voice_system import VoiceSystem
from attributes import CREATOR, AI_ASSISTANT, ME
import termination
import web_search
import commands
import conversation
import json
import wikipedia

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def func(query):
    if "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower() or "no" in query.lower() or "nope" in query.lower() or "nothing" in query.lower():
        voice_Sys.speak(f"Ok, goodbye {ME}")
        exit()    
    elif commands.give_command(query) != 1:
        success = 1
    elif web_search.explore(query) != 1:
        success = 1
    elif conversation.chat(query) != 1:
        success = 0.5
    else:
        if query != "":
            try:
                query = query.replace("search ","")
                voice_Sys.speak(f"Searching {query} in wikipedia...")
                results = wikipedia.summary(query,sentences=3)
                voice_Sys.speak(results)
            except:
                voice_Sys.speak(f"There's no {query} in wikipedia.")
                query = ""
                success = 0
            success = 1

    if query != "" and success == 1:
        return termination.anything_else()