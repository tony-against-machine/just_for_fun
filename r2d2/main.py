import speech_recognition as sr
import webbrowser

speech_recognizer = sr.Recognizer()


def search_query():
    return webbrowser.open_new_tab('https://www.google.com/search?q={}'.format(query))


with sr.Microphone() as source:
    audio = speech_recognizer.listen(source)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU').lower()

if 'найди' in query:
    search_query()
else:
    print('действий нет')
