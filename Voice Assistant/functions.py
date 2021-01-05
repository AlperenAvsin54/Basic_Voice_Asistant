import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import webbrowser
import random
import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup

def record(ask = False): ## Sesimizi kaydettiğimiz fonksiyon
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR',)
        except sr.UnknownValueError:
            print('Dediğini anlayamadım')
        except sr.RequestError:
            print('Sistemde hata meydana geldi')
        return voice

def speak(string): ## Asistanın cevabını sese dönüştüren fonksiyon
    tts = gTTS(string, lang='tr', slow=0)
    rand = random.randint(1, 100000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def chat(): ## Küçük bir sohbet fonksiyonu
    speak("Tabiikide benimle sohbet edebilirsin.")
    answer = record().lower()

    listNasılsın = ['İyiyim sen nasılsın?' , 'Teşekkür ederim iyiyim.' , 'Sağol iyiyim']
    listKimsin = ['Senin sesli asistanınım.' , "Senin için çalışan birisiyim."]
    listBilgi = ['Python dili kullanılarak yazıldım.']

    if answer == 'nasılsın':
        nasılsın = random.choice(listNasılsın)
        speak(nasılsın)

    if answer == 'kimsin':
        kimsin = random.choice(listKimsin)
        speak(kimsin)

    if answer == 'bilgi ver':
        bilgi = random.choice(listBilgi)
        speak(bilgi)

def hour(): ## Saat kaç fonksiyonu
    if question == 'saat kaç':
        speak("Şuanda saat" + datetime.now().strftime('%H:%M'))


def search(): ## İnternette arama yapma fonksiyonu
    speak("Hangi platformda arama yapmak istiyorsun?")
    choose = record()

    if choose == 'Google':
        speak("Googleda neyi aratmamı istersin?")
        google = record().lower()
        googleUrl = 'https://google.com/search?q=' + google
        webbrowser.get().open(googleUrl)
        speak("İstediğin aramayı yaptım.")

    elif choose == 'YouTube':
        speak("Youtubeda neyi aratmamı istersin?")
        yt = record().lower()
        youtubeUrl = 'https://www.youtube.com/results?search_query=' + yt
        webbrowser.get().open(youtubeUrl)
        speak("İstediğin aramayı yaptım.")

    elif choose == 'Vikipedi':
        speak("Vikipedide neyi aratmamı istersin?")
        viki = record().lower()
        vikiUrl = 'https://tr.wikipedia.org/wiki/' + viki
        webbrowser.get().open(vikiUrl)
        speak("İstediğin aramayı yaptım.")
