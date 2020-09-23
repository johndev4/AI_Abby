import random
from voice_system import VoiceSystem
from attributes import CREATOR, AI_ASSISTANT, ME

voiceSys = VoiceSystem(AI_ASSISTANT, ME)

def get_username(ME):
    yes = 0
    no = 0
    voiceSys.speak("May I know your name?")

    while ME == "":
        query = voiceSys.listen()

        if "yes" == query.lower() or "yeah" == query.lower():
            if yes == 0:
                voiceSys.speak("So, what is your name?")
            elif yes == 3 or yes == 5:
                rand = random.randint(0, 2)
                if rand == 0:
                    voiceSys.speak("I'm asking your name.")
                elif rand == 1:
                    voiceSys.speak("You are like a broken stereo")
                else:
                    voiceSys.speak("What the fuck! Are you dumb?")

            elif yes > 1:
                voiceSys.speak("I'm asking your name.")

            yes += 1

        elif "no" == query.lower() or "nope" == query.lower() or "don't want" in query.lower():
            if no == 0:
                voiceSys.speak("Why not? In order to help you, you should give me your name.")
                voiceSys.speak("So, what is your name?"); no += 1
            elif no == 2:
                voiceSys.speak("Ok, that's it. I'm terminating the program. Good bye!")
                exit()

        elif "terminate the program" in query.lower() or "goodbye" in query.lower() or "terminate" in query.lower():
            voiceSys.speak(f"Ok, goodbye")
            exit()

        else:
            if "i'm " in query.lower() or "i am " in query.lower() or "my name is " in query.lower() or "hi " in query.lower() or "hello " in query.lower() or "yes " in query.lower() or "it's " in query.lower() or "it is " in query.lower():
                ME = __process_name__(ME, query)

            else:
                if query == "":
                    voiceSys.speak("I want to know your name first.")
                else:
                    temp_name = query.lower()
                    voiceSys.speak("Is that your name?")

                    while True:
                        query = voiceSys.listen()
                        
                        if "yes" in query.lower() or "yea" in query.lower() or "yup" in query.lower() or "yep" in query.lower():
                            ME = temp_name
                            break
                        elif "no" in query.lower() or "nope" in query.lower():
                            query = query.replace("no ", "")
                            if "i'm " in query.lower() or "i am " in query.lower() or "my name is " in query.lower() or "hi " in query.lower() or "hello " in query.lower() or "yes " in query.lower() or "it's " in query.lower() or "it is " in query.lower():
                                ME = __process_name__(ME, query)
                            else:
                                voiceSys.speak("So, what is your name?")
                            break
                        elif "" == query:
                            voiceSys.speak("Again, is that your name?")

                        else:
                            break
    
    return ME.title()

def __process_name__(ME, query):
    ME = __process_encapsulation__(query, "i'm")
    ME = __process_encapsulation__(ME, "i am")
    ME = __process_encapsulation__(ME, "my name is")
    ME = __process_encapsulation__(ME, "it's")
    ME = __process_encapsulation__(ME, "it is")
    ME = __process_encapsulation__(ME, "hi")
    ME = __process_encapsulation__(ME, "hello")
    return ME
    

def __process_encapsulation__(str1, str2):
    if str1.find(str2) != -1:
        loc = str1.find(str2)
        str1 = str1[loc:len(str1)] 
        str1 = str1.replace("i'm ", "")
        str1 = str1.replace("i am ", "")
        str1 = str1.replace("my name is ", "")
        str1 = str1.replace("it's ", "")
        str1 = str1.replace("it is ", "")
        str1 = str1.replace("hi ", "")
        str1 = str1.replace("hello ", "")
    return str1
