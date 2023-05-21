from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
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


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    reps = 0
    label2.config(text="")
    label.config(text="Timer")
    canvas.itemconfig(y, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps < 8:
        # count_down(15 * 60)
        if reps % 2 == 0:
            count_down(WORK_MIN)
            label.config(text="Work", fg=GREEN)
        else:
            count_down(SHORT_BREAK_MIN)
            label.config(text="Break", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN)
        label.config(text="Break", fg=RED)
        print(reps)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps, timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    if count > 0:
        canvas.itemconfig(y, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps < 9:
            sessions = math.floor(reps / 2)
            mark = ""
            for i in range(sessions):
                mark += "✔"
            label2.config(text=mark)
            # if reps % 2 == 0:
            # for i in range(reps/2):

            start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(bg=YELLOW, padx=100, pady=50)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_img)
y = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0, column=1)

label2 = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
label2.grid(row=3, column=1)

button1 = Button(text="start", highlightthickness=0, command=start_timer)
button1.grid(row=2, column=0)

button2 = Button(text="reset", highlightthickness=0, command=reset_timer)
button2.grid(row=2, column=2)

window.mainloop()
