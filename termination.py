from voice_system import VoiceSystem
import operations

def anything_else(attr):
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)
    while True:
        voice_Sys.speak("Do you have anything else?")
        query = voice_Sys.listen()
        
        if query != "" and not("yes" == query.lower() or "yea" == query.lower() or "yup" == query.lower() or "yep" == query.lower()):
            if query != "Sorry, I can't here you.":
                if operations.func(attr, query):
                    break

        elif "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower() or "no " in  query.lower() or "nope" in query.lower() or "nothing" in query.lower():
            voice_Sys.speak(f"Ok, goodbye {attr.ME}")
            exit()
        elif "yes" in query.lower() or "yea" in query.lower() or "yup" in query.lower() or "yep" in query.lower():
            voice_Sys.speak("What can I help you?")
            return True