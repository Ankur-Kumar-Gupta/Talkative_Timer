from datetime import datetime
from playsound import playsound
from gtts import gTTS


now = datetime.now()
cHour = str(now.hour)
cMin = str(now.minute)
time = ['Current time is ' , cHour , ' hour ' , cMin , ' minutes']


def convert(s):
    new = " "
    for x in s:
        new += x
    return new


timeTxt = convert(time)
fh = open("test.txt", "w")
myText = fh.write(timeTxt)
fh.close() 


fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
fh.close()


playsound('output.mp3')
print(timeTxt)
