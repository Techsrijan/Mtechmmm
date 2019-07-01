from gtts import gTTS
from playsound import playsound
tts = gTTS('Welcome you all in TechSrijan Consultancy services Private Limited Summer Training Program')
tts.save('hello.mp3')
playsound('hello.mp3')