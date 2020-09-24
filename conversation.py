from attributes import ME, CREATOR, AI_ASSISTANT
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
    
    elif "hello" == query.lower() or "hi" == query.lower() or f"hello {AI_ASSISTANT}" == query.lower() or f"hi {AI_ASSISTANT}" == query.lower():
        greet = ["Hi", "Hello"]
        random.shuffle(greet)
        voice_Sys.speak(f"{greet[0]} {ME}")
    
    elif "fuck you" in query.lower():
        fuck = [f"Fuck you too {ME}", "You're so mean!", "You're so rude!"]
        random.shuffle(fuck)
        voice_Sys.speak(f"{fuck[1]}")

    elif "love you" in query.lower():
        love = [f"I love you too {ME}", "Oh, you are sweet",
        "I think I fell in love with you too."]
        random.shuffle(love)
        voice_Sys.speak(f"{love[1]}")

    elif "what" == query.lower():
        voice_Sys.speak("What do you mean?")

    elif "who" == query.lower():
        voice_Sys.speak("Who who?")
    
    elif "who are you" in query.lower() or "your name" in query.lower():
        blank = ["", ", your beautiful virtual assistant.", ", your girlfriend. Just kidding!", ", the smartest amongst virtual assistant."]
        random.shuffle(blank)
        voice_Sys.speak(f"I'm Abby{blank[1]}")
    
    elif "who am i" == query.lower() or "who i am" == query.lower():
        voice_Sys.speak(f"Your name is {ME}")
    
    elif "i am" in query.lower() or "i'm" in query.lower() or "my name is" in query.lower():
        temp_name = query.replace("i am ", "")
        temp_name = temp_name.replace("i'm ", "")
        temp_name = temp_name.replace("my name is ", "")
        voice_Sys.speak(f"Do you want me to call you you {temp_name}")
    
    else:
        return 1