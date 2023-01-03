import wikipedia
from voice_system import VoiceSystem

def explore(attr, query):
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)

    if "who is your creator" in query.lower():
        voice_Sys.speak(f"{attr.CREATOR} is my creator. He built me with python language on September 19, 2020")

    elif f"who is {attr.CREATOR}".lower() in query.lower():
        voice_Sys.speak(f"{attr.CREATOR} is the one who built me. He built me with python language on September 19, 2020")
    
    elif "where " in query.lower() and "your name" in query.lower():
        voice_Sys.speak(f"According to {attr.CREATOR}, my name ({attr.AI_ASSISTANT}) was inspired by the ancient language \"Assembly Language\".")
        print("A-ssem-B-l-Y = ABBY\r\n")
    
    elif "what" in query.lower() and "you made of" in query.lower():
        voice_Sys.speak(f"I'm made of bunch of \"python\"")
    
    elif "what" in query.lower() and "my name" in query.lower():
        voice_Sys.speak(f"As you said, You are {attr.ME}")
    
    elif "you" in query.lower() and "can" in query.lower() and "do" in query.lower():
        voice_Sys.speak("I can do these things:")
        print("1. Openning chrome")
        print("2. Search somesthing for you")
        print("3. Play music")
        print("4. Have a conversation with you\n")
    
    elif "search " in query.lower() or "search for " in query.lower() or "who is " in query.lower() or "who are " in query.lower() or "what is " in query.lower() or "what are " in query.lower():
        try:
            query = query.replace("search ","")
            query = query.replace("search for ","")
            query = query.replace("who is ","")
            query = query.replace("who are ","")
            query = query.replace("what is ","")
            query = query.replace("what are ","")
            voice_Sys.speak(f"Searching {query} in wikipedia...")
            results = wikipedia.summary(query,sentences=3)
            voice_Sys.speak(results)
        except:
            voice_Sys.speak(f"There's no {query} in wikipedia.")
            query = ""
    
    else:
        return 1