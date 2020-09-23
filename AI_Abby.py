#AI_Abby
#version 1.19-22alpha
#Author: John Mistica
# Duration created: September 19-22, 2020

from attributes import AI_ASSISTANT, CREATOR, ME
from voice_system import VoiceSystem
import operations
from get_started import get_username

print("Initializing the program...\r\n")

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

voice_Sys.speak(f"Hello, I'm {AI_ASSISTANT}, your virtual assistant.")
ME = get_username(ME)
voice_Sys.greet(ME)
voice_Sys.speak(f"What can I help you today?")

while True:
    query = voice_Sys.listen()
    operations.func(query)
