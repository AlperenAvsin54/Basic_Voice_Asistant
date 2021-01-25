import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import webbrowser
import random
import os
from datetime import datetime

def record(ask = False): ## Sesimizi kaydettiğimiz fonksiyon
    r = sr.Recognizer()
    while True:
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
    rand = random.randint(1, 100000000)
    file = 'audio-' + str(rand) + '.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def hour(): ## Saat kaç fonksiyonu
    speak("Şuanda saat" + datetime.now().strftime('%H:%M'))

def search(): ## İnternette arama yapma fonksiyonu
    speak("Hangi platformda arama yapmak istiyorsun?")
    platformlist = ["Google","YouTube","Vikipedi"]
    choose = record()

    if choose in platformlist:
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
    else:
        speak("Bu platformu bulamadım. İstersen Googleda aratabilirim.")
        question = record()
        if question == "evet":
            webbrowser.get().open('https://google.com/search?q=' + choose)
        else:
            print("Görüşürüz.")
        exit()