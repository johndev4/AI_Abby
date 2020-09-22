from voice_system import VoiceSystem
from attributes import CREATOR, AI_ASSISTANT, ME

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def anything_else():
    while True:
        voice_Sys.speak("Do you have anything else?")
        query = voice_Sys.listen()
        
        if "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower() or "no" in  query.lower() or "nope" in query.lower() or "nothing" in query.lower():
            voice_Sys.speak(f"Ok, goodbye {ME}")
            exit()
        elif "yes" in query.lower() or "yea" in query.lower() or "yup" in query.lower() or "yep" in query.lower():
            voice_Sys.speak("What can I help you?")
            break

        elif query != "":
            if query != "Sorry, I can't here you.":
                voice_Sys.speak("Please answer yes or no only.")