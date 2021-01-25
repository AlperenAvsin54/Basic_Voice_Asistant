#@author AlperenAvşin
#github = https://github.com/AlperenAvsin54

from functions import record,speak,hour,search
import random
import tkinter as tk
from tkinter.ttk import *

nasilsinList = ['nasılsın','iyi misin','nasıl gidiyor']
nasilsinCevap = ['Sağ ol iyiyim','İyiyim','Çok iyiyim']
tesekkürList = ['teşekkürler','teşekkür ederim','Sağ ol']
tesekkürCevap = ['Bir şey değil','Beğendiğine sevindim']
aramaList = ['arama yap','arama yaparmısın','internette ara','internette ararmısın']
cıkısList = ['çıkış yap','kendini kapat','görüşürüz','görüşmek üzere','bay bay','sonra görüşürüz']

def message():
    speak("Sana nasıl yardım edebilirim?")
    while True:  ## Fonksiyonların çalıştığı kısım. Durmaması için while döngüsüne aldım.
        voice = record()
        print(voice)

        if voice in nasilsinList:
            speak(random.choice(nasilsinCevap))

        if voice in tesekkürList:
            speak(random.choice(tesekkürCevap))

        if voice in aramaList:
            search()

        if 'saat kaç' in voice:
            hour()

        if voice in cıkısList:
            speak("Görüşürüz")
            exit()

window = tk.Tk()
window.title("Sesli Asistan")
window.geometry("400x200")
window.resizable(False,False)
yazi = tk.Label(window,text="Konuşmak için butona bas!", fg="black", font=("Open Sans", "20", "bold"))
buton = tk.Button(window,text="Konuş!", command=message, width="30", height="10")
yazi.pack()
buton.pack()
tk.mainloop()
