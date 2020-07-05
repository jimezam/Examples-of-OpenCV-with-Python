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
    # https://pyttsx3.readthedocs.io/en/latest/engine.html#pyttsx3.voice.Voice
    print (f'id: "{voice.id}"; name: "{voice.name}"; gender: "{voice.gender}".' )

# Wait while the text-to-speech engine is working
engine.runAndWait()

'''
This are the available voices found on Linux Mint 20.0 using eSpeak 1.48.04+dfsg-8build1

id: "afrikaans"; name: "afrikaans"; gender: "male".
id: "aragonese"; name: "aragonese"; gender: "male".
id: "bulgarian"; name: "bulgarian"; gender: "None".
id: "bosnian"; name: "bosnian"; gender: "male".
id: "catalan"; name: "catalan"; gender: "male".
id: "czech"; name: "czech"; gender: "male".
id: "welsh"; name: "welsh"; gender: "male".
id: "danish"; name: "danish"; gender: "male".
id: "german"; name: "german"; gender: "male".
id: "greek"; name: "greek"; gender: "male".
id: "default"; name: "default"; gender: "male".
id: "english"; name: "english"; gender: "male".
id: "en-scottish"; name: "en-scottish"; gender: "male".
id: "english-north"; name: "english-north"; gender: "male".
id: "english_rp"; name: "english_rp"; gender: "male".
id: "english_wmids"; name: "english_wmids"; gender: "male".
id: "english-us"; name: "english-us"; gender: "male".
id: "en-westindies"; name: "en-westindies"; gender: "male".
id: "esperanto"; name: "esperanto"; gender: "male".
id: "spanish"; name: "spanish"; gender: "male".
id: "spanish-latin-am"; name: "spanish-latin-am"; gender: "male".
id: "estonian"; name: "estonian"; gender: "None".
id: "persian"; name: "persian"; gender: "None".
id: "persian-pinglish"; name: "persian-pinglish"; gender: "None".
id: "finnish"; name: "finnish"; gender: "male".
id: "french-Belgium"; name: "french-Belgium"; gender: "male".
id: "french"; name: "french"; gender: "male".
id: "irish-gaeilge"; name: "irish-gaeilge"; gender: "None".
id: "greek-ancient"; name: "greek-ancient"; gender: "male".
id: "hindi"; name: "hindi"; gender: "male".
id: "croatian"; name: "croatian"; gender: "male".
id: "hungarian"; name: "hungarian"; gender: "male".
id: "armenian"; name: "armenian"; gender: "male".
id: "armenian-west"; name: "armenian-west"; gender: "male".
id: "indonesian"; name: "indonesian"; gender: "male".
id: "icelandic"; name: "icelandic"; gender: "male".
id: "italian"; name: "italian"; gender: "male".
id: "lojban"; name: "lojban"; gender: "None".
id: "georgian"; name: "georgian"; gender: "None".
id: "kannada"; name: "kannada"; gender: "None".
id: "kurdish"; name: "kurdish"; gender: "male".
id: "latin"; name: "latin"; gender: "male".
id: "lingua_franca_nova"; name: "lingua_franca_nova"; gender: "male".
id: "lithuanian"; name: "lithuanian"; gender: "male".
id: "latvian"; name: "latvian"; gender: "male".
id: "macedonian"; name: "macedonian"; gender: "male".
id: "malayalam"; name: "malayalam"; gender: "male".
id: "malay"; name: "malay"; gender: "male".
id: "nepali"; name: "nepali"; gender: "male".
id: "dutch"; name: "dutch"; gender: "male".
id: "norwegian"; name: "norwegian"; gender: "male".
id: "punjabi"; name: "punjabi"; gender: "None".
id: "polish"; name: "polish"; gender: "male".
id: "brazil"; name: "brazil"; gender: "male".
id: "portugal"; name: "portugal"; gender: "male".
id: "romanian"; name: "romanian"; gender: "male".
id: "russian"; name: "russian"; gender: "male".
id: "slovak"; name: "slovak"; gender: "male".
id: "albanian"; name: "albanian"; gender: "male".
id: "serbian"; name: "serbian"; gender: "male".
id: "swedish"; name: "swedish"; gender: "male".
id: "swahili-test"; name: "swahili-test"; gender: "male".
id: "tamil"; name: "tamil"; gender: "male".
id: "turkish"; name: "turkish"; gender: "male".
id: "vietnam"; name: "vietnam"; gender: "male".
id: "vietnam_hue"; name: "vietnam_hue"; gender: "male".
id: "vietnam_sgn"; name: "vietnam_sgn"; gender: "male".
id: "Mandarin"; name: "Mandarin"; gender: "male".
id: "cantonese"; name: "cantonese"; gender: "male".
Full dictionary is not installed for 'ru'
Full dictionary is not installed for 'zhy'
'''
