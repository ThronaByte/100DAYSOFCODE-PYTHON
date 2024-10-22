from tkinter import *
from math import floor
import time
import pygame

# Initialize pygame for sounds
pygame.mixer.init()

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
paused = False  # Pause state
time_left = 0  # Variable to store remaining time during pause

# Sounds (Replace with paths to your own sound files)
# start_sound = "./WEEK 4/Day 28/start_work.wav"
# break_sound = "./WEEK 4/Day 28/start_break.wav"

# ==========================RESET TIMER==============#
def reset_timer():
    global reps, paused
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    check_button.config(text="")
    task_input.delete(0, END)  # Clear task input on reset
    reps = 0
    paused = False

# ===================TIMER MECHANISM==================#
def start_timer():
    global reps, paused
    reps += 1
    paused = False

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        pygame.mixer.music.load(break_sound)
        pygame.mixer.music.play(loops=0)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        pygame.mixer.music.load(break_sound)
        pygame.mixer.music.play(loops=0)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        pygame.mixer.music.load(start_sound)
        pygame.mixer.music.play(loops=0)

# ===================COUNT-DOWN MECHANISM================#
def count_down(count):
    global time_left, paused
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 and not paused:
        global timer
        time_left = count  # Update remaining time
        timer = window.after(1000, count_down, count - 1)
    elif paused:
        time_left = count  # Store remaining time during pause
    else:
        start_timer()
        marks = ""
        for _ in range(floor(reps / 2)):
            marks += "✔"
        check_button.config(text=marks)

# ===================PAUSE/RESUME FUNCTION================#
def pause_resume_timer():
    global paused
    if not paused:
        paused = True
        window.after_cancel(timer)  # Pause the timer
        pause_button.config(text="Resume")
    else:
        paused = False
        pause_button.config(text="Pause")
        count_down(time_left)  # Resume countdown

# =============================UI SET-UP========================== #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title Label
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

# Canvas for timer text and pomodoro image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file='./WEEK 4/Day 28/pomodoro.png')
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Task input label
task_label = Label(text="Task:", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
task_label.grid(column=0, row=2)

# Task input field
task_input = Entry(width=30)
task_input.grid(column=1, row=2)

# Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

# Pause/Resume Button
pause_button = Button(text="Pause", highlightthickness=0, command=pause_resume_timer)
pause_button.grid(column=1, row=3)

# Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=3)

# Check Button (for displaying check marks)
check_button = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)
check_button.grid(column=1, row=4)

window.mainloop()
