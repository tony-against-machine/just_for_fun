import speech_recognition as sr
import actions
from bs4 import BeautifulSoup
import requests

speech_recognizer = sr.Recognizer()


weather_url = 'https://yandex.ru/pogoda/'
URL = requests.get(weather_url)
soup = BeautifulSoup()

search_query = 'найди'

with sr.Microphone() as source:
    audio = speech_recognizer.listen(source)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU')

copy_query = query.lower().split()

for i_word in copy_query:
    if i_word == search_query:
        copy_query.remove(search_query)
        search_obj = '+'.join(copy_query)
        actions.search_query(search_obj=search_obj)
