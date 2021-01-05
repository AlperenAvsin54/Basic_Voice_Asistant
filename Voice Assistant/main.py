# @author AlperenAvşin
# girhub = https://github.com/AlperenAvsin54

from functions import record,speak,askQuestion,search,chat

speak("Sana nasıl yardım edebilirim?")

while True:  ## Fonksiyonların çalıştığı kısım. Durmaması için while dögüsüne aldım.
    voice = record()
    print(voice)

    if 'sohbet' in voice:
        chat()

    if 'arama yap' in voice:
        search()

    if 'soru' in voice:
        askQuestion()

    if 'çıkış yap' in voice:
        speak("Görüşürüz")
        exit()
