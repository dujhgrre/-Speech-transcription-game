import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random

hallo = input("Приветсвую, это переводчик/перевести устную речь в текст.o(*￣▽￣*)o \n " \
"выберите, если вы хотите устную речь в текст перевести напишите 1, если перевести текст на иностранный язык то напишите 2, если устную речь перевести на иностранный язык пишите 3, если хотите попроьовать сыграть в игру то напишите 4:    ")


duration = 10  # секунды записи
sample_rate = 44100

if hallo == "1":
    print("Говори...┬┴┬┴┤(･_├┬┴┬┴")
    recording = sd.rec(
                int(duration * sample_rate), # длительность записи в сэмплах
                samplerate=sample_rate,      # частота дискретизации
                channels=1,                  # 1 — это моно
                dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи
    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал:", text)
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")

elif hallo == "2":
    language = input("выбери язык, вот список: \n"
                    "Английский - en \n"
                    "Испанский - es \n"
                    "Русский - ru \n"
                    "Португальский - pt \n"
                    "Индонезийский - id \n"
                    "Польский - pl \n"
                    "Итальянский - it \n"
                    "Турецкий - tr \n"
                   )

    translator = Translator()
    text = input("скиньте ваш текст:    ")
    translated = translator.translate(text, dest=language)  # здесь 'en' — это английский
    print("🌍 Перевод на выбранный вами язык:", translated.text)

elif hallo == "3":
    languages = input("выбери язык, вот список: \n"
                    "Английский - en \n"
                    "Испанский - es \n"
                    "Русский - ru \n"
                    "Португальский - pt \n"
                    "Индонезийский - id \n"
                    "Польский - pl \n"
                    "Итальянский - it \n"
                    "Турецкий - tr \n"
                   )
    print("Говори...∑( 口 ||")
    recording = sd.rec(
                int(duration * sample_rate), # длительность записи в сэмплах
                samplerate=sample_rate,      # частота дискретизации
                channels=1,                  # 1 — это моно
                dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи
    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")
    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        translator = Translator()
        translated = translator.translate(text, dest=languages)  # здесь 'en' — это английский
        print("🌍 Перевод на выбранный вами язык:", translated.text)
    except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
        print("Не удалось распознать речь.")
    except sr.RequestError as e:             # - если нет интернета или API недоступен
        print(f"Ошибка сервиса: {e}")


elif hallo == "4":
    couns = 0
    level1 = {"время    ":"time", "настоящее    ":"present","прошлое    ":"past","будущее   ":"future","день    ":"day","ночь   ":"night","после    ":"after","снова    ":"again","весна    ":"spring","осень   ":"autumn",}
    level2 = {"вызов    ":"Challenge","знание   ":"Knowledge","возможность  ":"Opportunity","лидерство  ":"Leadership   ","власть":"Authority   ","Команда  ":"Team","Дядя  ":"Uncle","Офис     ":"Office","Решение     ":" Solution","Успех    ":"Success",}
    level3 = {"Результат    ":"Outcome","Менталитет ":"Mentality","Вездесущность    ":"Ubiquity","Пренебрежение     ":"Neglect","Апелляция, обжалование     ":"Appeal"}
    print("игра заключается в том что вам дается слово и вы должны его перевести на англиский язык сказать лиюо написать.")
    game = input("выберите как вы хотите играть, если писать то 1 если говорить то 2:   ")
    level = input("теперь выберите сложность. \n"
                    "легкий уровень пишите -- 1 \n" \
                    "средний уровень пишите -- 2 \n" \
                    "сложный уровень пишите -- 3 \n"
                )

    if game == "1":
        if level == "1":
            print("начинаем!")
            for i in range(8):
                iop = input(random.choice(list(level1.keys())))
                if iop == level1.values():
                    print("правильно!")
                    couns += 2
                else:
                    print("неверно")
                    couns += 0
            print(couns)

        elif level == "2":
            print("начинаем!")
            for i in range(8):
                iop2 = input(random.choice(list(level2.keys())))
                if iop2 == level2.values():
                    print("правильно!")
                    couns += 4
                else:
                    print("неверно")
                    couns += 0
            print(couns)

        elif level == "3":
            print("начинаем!")
            for i in range(8):
                iop3 = input(random.choice(list(level3.keys())))
                if iop3 == level3.values():
                    print("правильно!")
                    couns += 6
                else:
                    print("неверно")
                    couns += 0
            print(couns)
    
    elif game == "2":
        print("начнем!")
        if level == "1":
            for i in range(8):
                iop2 = random.choice(list(level1.keys()))
                print(iop2)
                print("Говори...┬┴┬┴┤(･_├┬┴┬┴")
                recording = sd.rec(
                            int(duration * sample_rate), # длительность записи в сэмплах
                            samplerate=sample_rate,      # частота дискретизации
                            channels=1,                  # 1 — это моно
                            dtype="int16")               # формат аудиоданных
                sd.wait()  # ждём завершения записи
                wav.write("output.wav", sample_rate, recording)
                #print("Запись завершена, теперь распознаём...")
                recognizer = sr.Recognizer()
                with sr.AudioFile("output.wav") as source:
                    audio = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio, language="en-EN")
                    
                    #print("Ты сказал:", text)
                except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
                    print("Не удалось распознать речь.")
                except sr.RequestError as e:             # - если нет интернета или API недоступен
                    print(f"Ошибка сервиса: {e}")

                if level1[iop2] == text:
                    print("правильно!")
                    couns += 2
                else:
                    print("неверно")
                    couns += 0
            print(couns)
        
        elif level == "2":
            for i in range(8):
                iop2 = random.choice(list(level2.keys()))
                print(iop2)
                print("Говори...┬┴┬┴┤(･_├┬┴┬┴")
                recording = sd.rec(
                            int(duration * sample_rate), # длительность записи в сэмплах
                            samplerate=sample_rate,      # частота дискретизации
                            channels=1,                  # 1 — это моно
                            dtype="int16")               # формат аудиоданных
                sd.wait()  # ждём завершения записи
                wav.write("output.wav", sample_rate, recording)
                #print("Запись завершена, теперь распознаём...")
                recognizer = sr.Recognizer()
                with sr.AudioFile("output.wav") as source:
                    audio = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio, language="en-EN")
                    #print("Ты сказал:", text)
                except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
                    print("Не удалось распознать речь.")
                except sr.RequestError as e:             # - если нет интернета или API недоступен
                    print(f"Ошибка сервиса: {e}")

                if level1[iop2] == text:
                    print("правильно!")
                    couns += 4
                else:
                    print("неверно")
                    couns += 0
            print(couns)

        elif level == "3":
            for i in range(8):
                iop2 = random.choice(list(level3.keys()))
                print(iop2)
                print("Говори...┬┴┬┴┤(･_├┬┴┬┴")
                recording = sd.rec(
                            int(duration * sample_rate), # длительность записи в сэмплах
                            samplerate=sample_rate,      # частота дискретизации
                            channels=1,                  # 1 — это моно
                            dtype="int16")               # формат аудиоданных
                sd.wait()  # ждём завершения записи
                wav.write("output.wav", sample_rate, recording)
                #print("Запись завершена, теперь распознаём...")
                recognizer = sr.Recognizer()
                with sr.AudioFile("output.wav") as source:
                    audio = recognizer.record(source)

                try:
                    text = recognizer.recognize_google(audio, language="en-EN")
                 
                    #print("Ты сказал:", text)
                except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
                    print("Не удалось распознать речь.")
                except sr.RequestError as e:             # - если нет интернета или API недоступен
                    print(f"Ошибка сервиса: {e}")

                if level1[iop2] == text:
                    print("правильно!")
                    couns += 6
                else:
                    print("неверно")
                    couns += 0
            print(couns)
