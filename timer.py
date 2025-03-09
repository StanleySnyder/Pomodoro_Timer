import time
import os
import pygame

def play_sound(sound_file):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Ждем завершения проигрывания
            time.sleep(0.1)
    except Exception as e:
        print("Ошибка воспроизведения звука:", e)

def get_user_input(prompt, default):
    user_input = input(f"{prompt} (Enter для {default} мин): ")
    return int(user_input) if user_input.isdigit() else default

def pomodoro_timer():
    work_duration = get_user_input("Введите длительность рабочего времени в минутах", 25)
    short_break = get_user_input("Введите длительность короткого перерыва в минутах", 5)
    long_break = get_user_input("Введите длительность долгого перерыва в минутах", 15)
    cycles = get_user_input("Введите количество рабочих циклов перед долгим перерывом", 4)
    
    while True:
        for cycle in range(1, cycles + 1):
            print(f"\n🔴 Цикл {cycle}: Работаем {work_duration} минут...")
            play_sound("work_start.wav")
            countdown(work_duration * 60)
            
            print(f"\n🔔 Время работы окончено!", end=" ")
            
            if cycle < cycles:
                print(f"\n🟢 Время на короткий перерыв: {short_break} минут...")
                play_sound("short_break.wav")
                countdown(short_break * 60)
        
        print("\n💤 Долгий отдых: {long_break} минут...")
        play_sound("long_break.wav")
        countdown(long_break * 60)
        print("\n🔄 Начинаем новый цикл!")


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Время вышло!         ")

if __name__ == "__main__":
    pomodoro_timer()
