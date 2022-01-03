from gtts import gTTS
import os 

mytext="Lionel Andrés Messi is an Argentine professional footballer who plays for and captains the Argentina national team."
texts="hello messi"
language='en'

output=gTTS(text=texts and mytext,lang=language,slow=False)

output.save("output.mp3")
os.system("start output.mp3")