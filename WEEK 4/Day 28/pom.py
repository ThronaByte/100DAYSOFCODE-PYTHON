from tkinter import *

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

# ==========================RESET TIMER==============#
# TODO: 4 RESET TIMER
def reset_timer():
    """Function to reset timer"""
    window.after_cancel(timer)  # Changed to 'window'
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
    check_button.config(text="")
    global reps
    reps = 0

# ==========================RESET TIMER==============#


# ===================TIMER MECHANISM==================#
# TODO: 3 TIMER MECHANISM
def start_timer():
    """Function to start timer"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="BREAK", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="BREAK", fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

# ===================TIMER MECHANISM==================#


# ===================COUNT-DOWN MECHANISM================#
# TODO: 2 COUNT-DOWN MECHANISM
def count_down(count):
    """Count down function"""
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_button.config(text=marks)

# ===================COUNT-DOWN MECHANISM================#


# =============================UI SET-UP========================== #
# TODO: 1 UI SET-UP
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# TITLE
title_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

# CANVAS
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file='pomodoro.png')
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 128, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# RESET BUTTON
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# RESTART BUTTON
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# CHECK BUTTON
check_button = Label(text="", fg=GREEN, bg=YELLOW, highlightthickness=0)  # Changed from Button to Label
check_button.grid(column=1, row=3)
# =============================UI SET-UP========================== #

window.mainloop()
