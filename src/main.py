# AI Abby Virtual Assistant [Version 1.19-22alpha]
# (c) 2020, AI Abby Virtual Assistant. All Rights Reserved.
# Author: Johndev4
# Created: September 19-22, 2020

print("Initializing the program...")

from os import system
system('title AI Abby Virtual Assistant')

from attributes import Attributes
from voice_system import VoiceSystem
from get_started import get_username
import operations

if __name__ == "__main__":
    attr = Attributes()
    voice_Sys = VoiceSystem(attr.AI_ASSISTANT, attr.ME)

    system('cls')
    print(f"{attr.HEAD}\r\n\r\n")
    
    voice_Sys.speak(f"Hello, I'm {attr.AI_ASSISTANT}, your virtual assistant.")
    attr.ME = get_username(attr)
    voice_Sys.greet(attr.ME)
    voice_Sys.speak(f"What can I help you today?")

    while True:
        query = voice_Sys.listen()
        operations.func(attr, query)
