import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

strTime = datetime.datetime.now().strftime("%H:%M:%S")    
speak(f"the time is {strTime}")
