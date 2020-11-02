import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import webbrowser
import random
import os
from datetime import datetime

def speak(string):
    tts = gTTS(string,lang='en',slow=0)
    rand = random.randint(1,100000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

class Assistant():
    speak("How can i help you?")
    def __init__(self, voice):
        self.voice = voice

    def record(ask = False):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if ask:
                print(ask)
            audio = r.listen(source)
            voice = ''
            try:
                voice = r.recognize_google(audio , language='en')
            except sr.UnknownValueError:
                print("I couldn't understand")
            except sr.RequestError:
                print('An error has occurred in the system')
            return voice

    def searchInNet(voice):
        search = record("What will you search?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)


    def searchInWikipedia():
        wikiSearch = record("What will you search?")
        wikiUrl = 'https://tr.wikipedia.org/wiki/' + wikiSearch
        webbrowser.get().open(wikiUrl)


    def response(voice):
        def record(ask = False):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                if ask:
                    print(ask)
                audio = r.listen(source)
                voice = ''
                try:
                    voice = r.recognize_google(audio , language='en')
                except sr.UnknownValueError:
                    print('Dediğini anlayamadım')
                except sr.RequestError:
                    print('Sistemde hata meydana geldi')
                return voice

        def searchInNet():
            search = record("What will you search?")
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)


        def searchInWikipedia():
            wikiSearch = record("What will you search?")
            wikiUrl = 'https://tr.wikipedia.org/wiki/' + wikiSearch
            webbrowser.get().open(wikiUrl)


        if 'what time is it' in voice:
            speak("Hour is" + datetime.now().strftime('%H:%M') + "now")


        if 'search in Wikipedia' in voice:
            searchInWikipedia()

        if 'search in net' in voice:
            searchInNet()

        if 'how are you' in voice:
            speak("Thanks i am good.")

        elif 'bye' in voice:
            speak("See you later")
            exit()

    while 1:
        voice = record()
        print(voice)
        response(voice)
