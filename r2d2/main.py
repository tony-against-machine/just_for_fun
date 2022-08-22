import speech_recognition as sr
import actions

speech_recognizer = sr.Recognizer()

with sr.Microphone() as source:
    audio = speech_recognizer.listen(source)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU').lower().split()

for word in query:
    if word == 'найди':
        query.remove('найди')
        search_obj = '+'.join(query)
        actions.search_query(search_obj=search_obj)
    else:
        print('настрой нормально звук и цикл')
