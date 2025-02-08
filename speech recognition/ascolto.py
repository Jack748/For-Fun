import speech_recognition as sr
from os import path
from pydub import AudioSegment


src = "se.opus"
dst = "test.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_file(src)
sound.export(dst, format="wav")

file = path.join(path.dirname(path.realpath(__file__)), "test.wav")
r = sr.Recognizer()

with sr.AudioFile(file) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    print("finito di leggere")
    text = r.recognize_google(audio, language="it-IT")
    print("GESU")

# with sr.Microphone() as source:
#     print("SPEAK!")
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)
#     print("ok, elaboro")

  

    
print(text)