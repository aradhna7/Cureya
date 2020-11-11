from gtts import gTTS
import os


fh = open("text.txt", "r")   #r for read w for write
myText = fh.read().replace("\n"," ")


language ='en'

output =gTTS(text=myText, lang=language, slow=False)   #highspeed sound

output.save("output.mp3")
fh.close()
os.system("start output.mp3")