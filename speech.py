import speech_recognition  as sr
r= sr.Recognizer()
 
with sr.Microphone()as source:
     print("who are you??")
     audio= r.listen(source)
     
     
try:
    print("Hi! Mr.",r.recognize_google(audio))
except:
    print("unable to recognition your voice")       