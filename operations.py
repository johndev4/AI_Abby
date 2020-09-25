from voice_system import VoiceSystem
import termination
import web_search
import commands
import conversation
import json
import wikipedia

def func(attr, query):
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)

    if "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower() or "no" in query.lower() or "nope" in query.lower() or "nothing" in query.lower():
        voice_Sys.speak(f"Ok, goodbye {attr.ME}")
        exit()
    
    elif conversation.chat(attr, query) != 1:
        success = 0.5
    elif web_search.explore(attr, query) != 1:
        success = 1
    elif commands.give_command(attr, query) != 1:
        success = 1
    else:
        if query != "":
            try:
                voice_Sys.speak(f"Searching in wikipedia...")
                results = wikipedia.summary(query,sentences=3)
                voice_Sys.speak(results)
            except:
                voice_Sys.speak(f"There's no {query} in wikipedia.")
                query = ""
                success = 0
            success = 1

    if query != "" and success == 1:
        return termination.anything_else(attr)