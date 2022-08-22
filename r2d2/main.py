import speech_recognition as sr
import webbrowser

speech_recognizer = sr.Recognizer()


def search_query(search_obj):
    return webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(search_obj))


with sr.Microphone() as source:
    audio = speech_recognizer.listen(source)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU').lower().split()

for word in query:
    if word == 'найди':
        query.remove('найди')
        search_obj = '+'.join(query)
        search_query(search_obj=search_obj)
