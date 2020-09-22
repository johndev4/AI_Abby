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
            if ("i'm " or "i am " or "my name is " or "hi " or "hello " or "yes ") in query.lower():
                ME = query.replace("i'm ", "")
                ME = ME.replace("i am ", "")
                ME = ME.replace("my name is ", "")
                ME = ME.replace("hi ", "")
                ME = ME.replace("hello ", "")
                print("hellos")

            else:
                if query == "":
                    voiceSys.speak("I want to know your name first.")
                else:
                    temp_name = query.lower()
                    voiceSys.speak("Is that your name?")

                    while True:
                        query = voiceSys.listen()
                        
                        if "yes" == query.lower() or "yeah" == query.lower():
                            ME = temp_name
                            break
                        elif "no" == query.lower() or "nope" == query.lower():
                            voiceSys.speak("So what is your name?")
                            break
                        elif "Sorry, I can't here you." == query:
                            voiceSys.speak("Again, is that your name?")

                        else:
                            voiceSys.speak("Please answer yes or no only.")
    
    return ME.title()
