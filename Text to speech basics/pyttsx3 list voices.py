import pyttsx3

# Object creation of the engine
engine = pyttsx3.init()

# Get the system's available voices
voices = engine.getProperty('voices')

for voice in voices:
    # Activate the voices one by one
    engine.setProperty('voice', voice.id)
    
    # Text-to-speech the message to test the voice
    engine.say('Hola mundo')
    
    # Print the active's voice id
    print (voice.id)

# Wait while the text-to-speech engine is working
engine.runAndWait()

'''
This are the available voices found on Linux Mint 20.0 using Espeak 1.48.04+dfsg-8build1

afrikaans
aragonese
bulgarian
bosnian
catalan
czech
welsh
danish
german
greek
default
english
en-scottish
english-north
english_rp
english_wmids
english-us
en-westindies
esperanto
spanish
spanish-latin-am
estonian
persian
persian-pinglish
finnish
french-Belgium
french
irish-gaeilge
greek-ancient
hindi
croatian
hungarian
armenian
armenian-west
indonesian
icelandic
italian
lojban
georgian
kannada
kurdish
latin
lingua_franca_nova
lithuanian
latvian
macedonian
malayalam
malay
nepali
dutch
norwegian
punjabi
polish
brazil
portugal
romanian
russian
slovak
albanian
serbian
swedish
swahili-test
tamil
turkish
vietnam
vietnam_hue
vietnam_sgn
Mandarin
cantonese
'''
