import pyttsx3

#############################################################

infile = "message.txt"

fd = open(infile, 'r')

message = fd.read()

fd.close()

#############################################################

engine = pyttsx3.init('espeak', True)

engine.save_to_file(message, 'output.mp3')

engine.runAndWait()

#############################################################
