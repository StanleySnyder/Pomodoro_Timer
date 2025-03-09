import time
import os
import pygame
import tkinter as tk
from tkinter import StringVar
import threading

# Настройки цветов
dark_bg = "#1e1e1e"
red_accent = "#d32f2f"
text_color = "#ffffff"
green_accent = "#388e3c"

def play_sound(sound_file):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
    except Exception as e:
        print("Ошибка воспроизведения звука:", e)

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.iconbitmap("icon.ico")
        self.root.geometry("400x500")  # Увеличиваем высоту окна
        self.root.resizable(False, False)
        self.root.configure(bg=dark_bg)

        # Значения по умолчанию
        self.work_duration = 25 * 60
        self.short_break = 5 * 60
        self.long_break = 15 * 60
        self.cycles = 4
        self.current_cycle = 0
        self.running = False
        self.phase = "Работа"
        self.time_left = self.work_duration

        # Заголовок
        self.label = tk.Label(root, text="Помодоро Таймер", font=("Arial", 18, "bold"), fg=red_accent, bg=dark_bg)
        self.label.pack(pady=10)

        # Метка для отображения текущего этапа
        self.phase_label = tk.Label(root, text="Работаем", font=("Arial", 14, "bold"), fg=red_accent, bg=dark_bg)
        self.phase_label.pack(pady=5)

        # Отображение таймера
        self.timer_display = StringVar()
        self.timer_display.set(self.format_time(self.time_left))
        self.timer_label = tk.Label(root, textvariable=self.timer_display, font=("Arial", 24), fg=text_color, bg=dark_bg)
        self.timer_label.pack(pady=20)

        # Кнопки управления
        self.start_button = tk.Button(root, text="Старт", command=self.start_timer, bg=red_accent, fg=text_color)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.pause_button = tk.Button(root, text="Пауза", command=self.pause_timer, bg=red_accent, fg=text_color)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Сброс", command=self.reset_timer, bg=red_accent, fg=text_color)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        # Поля для ввода настроек
        self.work_label = tk.Label(root, text="Работа (мин):", font=("Arial", 12), fg=text_color, bg=dark_bg)
        self.work_label.pack(pady=5)
        self.work_entry = tk.Entry(root, font=("Arial", 12))
        self.work_entry.insert(0, str(self.work_duration // 60))  # Вставляем текущее значение
        self.work_entry.pack(pady=5)

        self.short_break_label = tk.Label(root, text="Короткий перерыв (мин):", font=("Arial", 12), fg=text_color, bg=dark_bg)
        self.short_break_label.pack(pady=5)
        self.short_break_entry = tk.Entry(root, font=("Arial", 12))
        self.short_break_entry.insert(0, str(self.short_break // 60))  # Вставляем текущее значение
        self.short_break_entry.pack(pady=5)

        self.long_break_label = tk.Label(root, text="Долгий перерыв (мин):", font=("Arial", 12), fg=text_color, bg=dark_bg)
        self.long_break_label.pack(pady=5)
        self.long_break_entry = tk.Entry(root, font=("Arial", 12))
        self.long_break_entry.insert(0, str(self.long_break // 60))  # Вставляем текущее значение
        self.long_break_entry.pack(pady=5)

        self.cycles_label = tk.Label(root, text="Количество циклов:", font=("Arial", 12), fg=text_color, bg=dark_bg)
        self.cycles_label.pack(pady=5)
        self.cycles_entry = tk.Entry(root, font=("Arial", 12))
        self.cycles_entry.insert(0, str(self.cycles))  # Вставляем текущее значение
        self.cycles_entry.pack(pady=5)

        # Кнопка для применения настроек
        self.apply_button = tk.Button(root, text="Применить настройки", command=self.apply_settings, bg=red_accent, fg=text_color)
        self.apply_button.pack(pady=10)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def update_timer(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.timer_display.set(self.format_time(self.time_left))
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.next_phase()

    def next_phase(self):
        if self.phase == "Работа":
            play_sound("work_start.wav")
            if self.current_cycle < self.cycles - 1:
                self.phase = "Короткий перерыв"
                self.time_left = self.short_break
                play_sound("short_break.wav")
                self.update_phase_label("Отдыхаем", green_accent)
            else:
                self.phase = "Долгий перерыв"
                self.time_left = self.long_break
                play_sound("long_break.wav")
                self.update_phase_label("Отдохни побольше", green_accent)
        elif self.phase in ["Короткий перерыв", "Долгий перерыв"]:
            self.phase = "Работа"
            self.time_left = self.work_duration
            self.current_cycle = (self.current_cycle + 1) % self.cycles
            play_sound("work_start.wav")
            self.update_phase_label("Работаем", red_accent)
        self.timer_display.set(self.format_time(self.time_left))
        self.running = True
        self.update_timer()

    def start_timer(self):
        if not self.running:
            play_sound("work_start.wav")
            self.running = True
            self.update_timer()

    def pause_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.current_cycle = 0
        self.phase = "Работа"
        self.time_left = self.work_duration
        self.timer_display.set(self.format_time(self.time_left))
        self.update_phase_label("Работаем", red_accent)

    def update_phase_label(self, text, color):
        self.phase_label.config(text=text, fg=color)

    def apply_settings(self):
        try:
            self.work_duration = int(self.work_entry.get()) * 60
            self.short_break = int(self.short_break_entry.get()) * 60
            self.long_break = int(self.long_break_entry.get()) * 60
            self.cycles = int(self.cycles_entry.get())
            self.time_left = self.work_duration
            self.current_cycle = 0
            self.phase = "Работа"
            self.timer_display.set(self.format_time(self.time_left))
            self.update_phase_label("Работаем", red_accent)
            print(f"Настройки применены: Работа = {self.work_duration // 60} мин, Короткий перерыв = {self.short_break // 60} мин, Долгий перерыв = {self.long_break // 60} мин, Количество циклов = {self.cycles}")
        except ValueError:
            print("Ошибка ввода. Пожалуйста, убедитесь, что все значения корректны.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
