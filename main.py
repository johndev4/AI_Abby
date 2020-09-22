from voice_system import VoiceSystem
import termination
import web_search
import commands
import conversation
from get_started import tell_your_name
from attributes import CREATOR, AI_ASSISTANT, ME
import json

print("Initializing the program...")

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

voice_Sys.speak(f"Hello, I'm {AI_ASSISTANT}, your virtual assistant.")
ME = tell_your_name(ME)
voice_Sys.greet(ME)
voice_Sys.speak(f"What can I help you today?")

while True:
    query = voice_Sys.listen()

    if "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower() or "no" in query.lower() or "nope" in query.lower() or "nothing" in query.lower():
        voice_Sys.speak(f"Ok, goodbye {ME}")
        exit()    
    elif commands.give_command(query) != 1:
        success = 1
    elif web_search.explore(query) != 1:
        success = 1
    elif conversation.chat(query) != 1:
        success = 1
    else:
        if query != "":
            voice_Sys.speak("Sorry, I'm still learning about that.")
            success = 0

    if query != "" and success == 1:
        termination.anything_else()