import random
from voice_system import VoiceSystem
from attributes import CREATOR, AI_ASSISTANT, ME

voiceSys = VoiceSystem(AI_ASSISTANT, ME)

def tell_your_name(ME):
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



        else:
            if "i'm " in query.lower() or "i am " in query.lower() or "my name is " in query.lower() or "hi " in query.lower() or "hello " in query.lower() or "yes " in query.lower() or "it's " in query.lower() or "it is " in query.lower():
                ME = __proccess_name__(ME, query)

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
                                ME = __proccess_name__(ME, query)
                            else:
                                voiceSys.speak("So, what is your name?")
                            break
                        elif "" == query:
                            voiceSys.speak("Again, is that your name?")

                        else:
                            break
    
    return ME.title()

def __proccess_name__(ME, query):
    ME = query.replace("i'm ", "")
    ME = ME.replace("i am ", "")
    ME = ME.replace("my name is ", "")
    ME = ME.replace("hi ", "")
    ME = ME.replace("hello ", "")
    ME = ME.replace("it's ", "")
    ME = ME.replace("it is ", "")
    ME = ME.split(" "); ME = ME[1]
    return ME