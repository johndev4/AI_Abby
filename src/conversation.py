from voice_system import VoiceSystem
import random
import get_started

def chat(attr, query):
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)

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
    
    elif "hello" == query.lower() or "hi" == query.lower() or f"hello {attr.AI_ASSISTANT}" == query.lower() or f"hi {attr.AI_ASSISTANT}" == query.lower():
        greet = ["Hi", "Hello"]
        random.shuffle(greet)
        voice_Sys.speak(f"{greet[0]} {attr.ME}")
    
    elif "fuck you" in query.lower():
        fuck = [f"Fuck you too {attr.ME}", "You're so mean!", "You're so rude!"]
        random.shuffle(fuck)
        voice_Sys.speak(f"{fuck[1]}")

    elif "love you" in query.lower():
        love = [f"I love you too {attr.ME}", "Oh, you are sweet",
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
        voice_Sys.speak(f"Your name is {attr.ME}")
    
    elif "i am" in query.lower() or "i'm" in query.lower() or "my name is" in query.lower():
        temp = get_started.__process_name__(query)

        if temp.title() != attr.ME:
            ans = [f"No, you are {attr.ME}", f"You lied to me. You said you are {attr.ME}",f"I thought you are {attr.ME}"]
            random.shuffle(ans)
            pick = random.choice(ans)
            voice_Sys.speak(pick)
        else:
            voice_Sys.speak(f"Hello {attr.ME}")
    
    else:
        return 1