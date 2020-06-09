import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
  print('Hi what you want?')
  audio = r.listen(source)
  voice_data = r.recognize_google(audio)
  print(voice_data)