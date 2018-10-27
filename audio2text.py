import speech_recognition as sr
import webbrowser as wb
 
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application.exe %s'

r = sr.Recognizer()

audio='welcome.wav'
with sr.AudioFile(audio) as source:
    print ('Say Something!')
    audio = r.record(source)
    print ('Done!')
 
try:
    text = r.recognize_google(audio)
    print(text)
    #wb.get(chrome_path).open(text)

    #lang = 'en'

    #speak.tts(text, lang)

    #text = 'https://www.google.co.in/search?q=' + text
    #wb.get(chrome_path).open(text)
 
except Exception as e:
    print (e)
