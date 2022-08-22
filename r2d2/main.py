import speech_recognition as sr
import re
import actions

speech_recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = speech_recognizer.listen(source)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU').lower()



if query == 'открой youtube':
    print(actions.open_web_browser())
if query == 'найди прогноз погоды':
    print(actions.search_query())
else:
    print('настрой нормально уровень шума и таймаут!')
