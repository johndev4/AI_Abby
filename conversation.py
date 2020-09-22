from constant_variables import ME, CREATOR, AI_ASSISTANT
import wikipedia
import random
from voice_system import VoiceSystem

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

def chat(query):

    if "what's up" in query.lower() or "what are you doing" in query.lower():
        doing = ["algorithm", "techie thing", "of my chores", "decoration for my new house"]
        random.shuffle(doing)
        voice_Sys.speak(f"Hi there, I'm doing some {doing[1]}. Let me know if you need something.")

    elif "hey" in query.lower():
        voice_Sys.speak("Hi, what can I do for you?")
        
    elif "how are you" in query.lower():
        feel = ["having a great day, thanks", "doing great, thanks", "feeling helpful", "a bit sad but don't worry"]
        random.shuffle(feel)
        voice_Sys.speak(f"I'm {feel[1]}.")
        if feel == "feeling helpful":
            voice_Sys.speak("What can I do for you?")

    elif "who are you" in query.lower():
        blank = ["", ", your beautiful virtual assistant.", ", your girlfriend. Just kidding!", ", the smartest among virtual assistant."]
        random.shuffle(blank)
        voice_Sys.speak(f"I'm Abby{blank[1]}")
    
    elif "hello" in query.lower() or "hi" in query.lower():
        greet = ["Hi", "Hello"]
        random.shuffle(greet)
        voice_Sys.speak(f"{greet[0]} {ME}")
    
    elif "f***" in query.lower() or "fuck you" in query.lower():
        voice_Sys.speak(f"Fuck you too!")
    
    else:
        return 1