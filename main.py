from attributes import AI_ASSISTANT, CREATOR, ME
from voice_system import VoiceSystem
import operation
from get_started import tell_your_name

print("Initializing the program...")

voice_Sys = VoiceSystem(AI_ASSISTANT, ME)

voice_Sys.speak(f"Hello, I'm {AI_ASSISTANT}, your virtual assistant.")
ME = tell_your_name(ME)
voice_Sys.greet(ME)
voice_Sys.speak(f"What can I help you today?")

while True:
    query = voice_Sys.listen()
    operation.func(query)  