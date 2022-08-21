import speech_recognition
import webbrowser
import re

speech_recognizer = speech_recognition.Recognizer()


def open_web_browser():
    return webbrowser.open('https://www.youtube.com/')


with speech_recognition.Microphone() as microphone:
    speech_recognizer.adjust_for_ambient_noise(source=microphone)
    audio = speech_recognizer.listen(source=microphone)
    query = speech_recognizer.recognize_google(audio_data=audio, language='ru-RU').lower()


if query == 'открой youtube':
    open_web_browser()
    print('Запуск youtube')
