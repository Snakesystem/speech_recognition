import speech_recognition as sr 
from time import ctime
import webbrowser
import time
from gtts import gTTS
import playsound
import os
import random

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='id')
    #r = random.randint(1, 10000000)
    audio_file = 'audio.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

r = sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        print("Katakan sesuatu, tapi jangan curhat !")
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='ms-id')
        except sr.UnknownValueError:
            speak('Maaf, aku tidak tau maksudmu')
        except sr.RequestError:
            speak('Maaf, lagi sariawan tidak bisa berbicara haha')
        return voice_data

def respon(voice_data):
    while True:
        audio_file = speak()
        print(audio_file)
        if 'siapa namamu' in voice_data:
            speak('Nama saya Ellie')
        elif 'jam berapa' in voice_data:
            speak(ctime())
        elif 'hai' in voice_data:
            speak('Iya Feri, ada yang bisa kubantu ?')
        elif 'cari' in voice_data:
            search = record_audio('Apa yang ingin kamu cari ?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            speak('Ini yang aku temukan ' + search)
        elif 'temukan lokasi' in voice_data:
            location = record_audio('Tempat mana yang ingin kamu cari ?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            speak('Ini tempat yang aku temukan ' + location)
        elif 'terimakasih' in voice_data:
            exit()

    time.sleep(1)
speak('Ada yang bisa aku bantu ?')
while 1:
    voice_data = record_audio()
    respon(voice_data)