# Day 28 Project - Pomodoro App
import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_SYMBOL = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
session = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global session
    start_button["state"] = "active"
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    for i in range(4):
        check_labels[i].config(text="")
    session = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start_button["state"] = "disabled"
    global session
    session += 1
    i = (session // 2) - 1

    if session in (1, 3, 5, 7):
        countdown(WORK_MIN * 60)
        status_label.config(text="Work", fg=RED)
    elif session in (2, 4, 6):
        countdown(SHORT_BREAK_MIN * 60)
        check_labels[i].config(text=f"{CHECK_SYMBOL}")
        check_labels[i].grid(column=session//2, row=4)
        status_label.config(text="Short Break", fg=PINK)
    elif session == 8:
        countdown(LONG_BREAK_MIN * 60)
        check_labels[i].config(text=f"{CHECK_SYMBOL}")
        check_labels[i].grid(column=4, row=4)
        status_label.config(text="Long Break")
    elif session == 9:
        session = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1, columnspan=4)

# Labels
status_label = tkinter.Label(text="Pomodoro App", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
status_label.grid(column=1, row=0, columnspan=4)

num1_label = tkinter.Label(text=f"1", font=(FONT_NAME, 15), bg=YELLOW)
num1_label.grid(column=1, row=3)
num2_label = tkinter.Label(text=f"2", font=(FONT_NAME, 15), bg=YELLOW)
num2_label.grid(column=2, row=3)
num3_label = tkinter.Label(text=f"3", font=(FONT_NAME, 15), bg=YELLOW)
num3_label.grid(column=3, row=3)
num4_label = tkinter.Label(text=f"4", font=(FONT_NAME, 15), bg=YELLOW)
num4_label.grid(column=4, row=3)
check_labels = []
for _ in range(4):
    check_labels.append(tkinter.Label(text=f"{CHECK_SYMBOL}", font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN))

# Buttons
start_button = tkinter.Button(text="Start", width=10, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(column=5, row=2)

window.mainloop()
