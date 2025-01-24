import speech_recognition as sr
import random
import time  

def recognize_speech_from_mic(language="en-EN"):
    recog = sr.Recognizer()
    with sr.Microphone() as mic:
        print("Говорите...")
        recog.adjust_for_ambient_noise(mic)
        audio = recog.listen(mic)

    try:
        return recog.recognize_google(audio, language=language)
    except (sr.UnknownValueError, sr.RequestError):
        return None

def play_game(level):
    words = {
    "easy": ["dairy", "mouse", "computer"],
    "medium": ["programming", "algorithm", "developer"],
    "hard": ["neural network", "machine learning", "artificial intelligence"]
    }

    if level not in words:
        print("Некорректный уровень сложности!")
        return

    score  = 0 
    attempts = 3
    print(f"Вы выбрали уровень: {level}. Попыток: {attempts}")
    time.sleep(1)  

    for _ in range(attempts):
        true_word = random.choice(words[level])
        print(f"Попробуйте сказать слово: {true_word}")

        recognized_word = recognize_speech_from_mic()
        if recognized_word == true_word.lower():
            print("Верно!")
            score += 1
        else:
            print("Неверно.")
        
        time.sleep(1)  

    print(f"Игра окончена. Ваш счет: {score}/{attempts}")

level = input("Выберите уровень сложности (easy, medium, hard): ")
play_game(level)
