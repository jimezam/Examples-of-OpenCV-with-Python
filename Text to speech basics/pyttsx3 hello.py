# sudo apt-get update && sudo apt-get install espeak
# pip3 install pyttsx3

import pyttsx3

# Object creation of the engine
# pyttsx3.init('sapi5') 
# pyttsx3.init('nsss') 
# pyttsx3.init('espeak')  # Default
engine = pyttsx3.init()

# Select a voice (optional)
engine.setProperty('voice', 'spanish-latin-am')

# Specify the message to be spoken
engine.say("¡Hola a todos! ¿cómo están?")

# Execute the requested tasks over the engine
engine.runAndWait()
