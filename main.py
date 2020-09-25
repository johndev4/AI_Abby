# AI Abby Virtual Assistant [Version 1.19-22alpha]
# (c) 2020, AI Abby Virtual Assistant. All Rights Reserved.
# Author: Johndev4
# Created: September 19-22, 2020

print("Initializing the program...")

from os import system
system('title AI Abby Virtual Assistant')

from attributes import AI_ASSISTANT, CREATOR, ME, HEAD
from voice_system import VoiceSystem
from get_started import get_username
import operations

if __name__ == "__main__":
    system('cls')
    print(f"{HEAD}\r\n\r\n")
    
    voice_Sys = VoiceSystem(AI_ASSISTANT, ME)
    
    voice_Sys.speak(f"Hello, I'm {AI_ASSISTANT}, your virtual assistant.")
    ME = get_username(ME)
    voice_Sys.greet(ME)
    voice_Sys.speak(f"What can I help you today?")

    while True:
        query = voice_Sys.listen()
        operations.func(query)
