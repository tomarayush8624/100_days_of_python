from tkinter import *
import pandas
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"

word_dict = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
data_dict = data.to_dict('records')


def next_card():
    global word_dict, flip
    try:
        window.after_cancel(flip)
    except ValueError:
        pass
    finally:
        canvas.itemconfig(background_img, image=card_front_img)
        canvas.itemconfig(title, text="French", fill="#000")
        word_dict = data_dict[2]
        canvas.itemconfig(word, text=f"{word_dict['French']}", fill="#000")
        flip = window.after(3000, translate)


def know():
    next_card()
    update_data()


def update_data():
    global word_dict
    data_dict.remove(word_dict)
    updated_df = pandas.DataFrame.from_records(data_dict)
    updated_df.to_csv("data/words_to_learn.csv", mode='w', index=False)


def translate():
    global word_dict
    canvas.itemconfig(title, text="English", fill="#fff")
    canvas.itemconfig(word, text=f"{word_dict['English']}", fill="#fff")
    canvas.itemconfig(background_img, image=card_back_img)


window = Tk()
window.title("Lang Learn")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip = None

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(400, 263, image=card_front_img)
title = canvas.create_text(400, 150, text="Title", font=("Aerial", 48, "italic"))
word = canvas.create_text(400, 263, text="WORD", font=("Aerial", 60, "bold"))
# print(type(word1))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
right_btn = Button(image=check_img, highlightthickness=0, command=know)
right_btn.grid(row=1, column=1)

window.mainloop()
