from tkinter import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"
current_card = {}
french_dict = {}


# -----------------------------------------------CREATE NEW FLASH CARDS--------------------------------------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    french_dict = french_words.to_dict(orient="records")
else:
    french_dict = data.to_dict(orient="records")


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(french_dict)
    french = current_card['French']
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french, fill="black")
    canvas.itemconfig(current_image, image=card_front_image)
    timer = window.after(3000, flash_cards)


def flash_cards():
    English = current_card['English']
    canvas.itemconfig(current_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill=WHITE)
    canvas.itemconfig(word_text, text=English, fill=WHITE)


def remove_card():
    french_dict.remove(current_card)
    data = pandas.DataFrame(french_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_card()


# --------------------------------------------------UI SETUP -----------------------------------------------------
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flash_cards)

# create canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file=".\images\card_front.png")
card_back_image = PhotoImage(file=".\images\card_back.png")
current_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# wrong button
wrong_image = PhotoImage(file=".\images\wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong.grid(row=1, column=0)

# right button
right_image = PhotoImage(file=".\images\wbutton_right.png")
right = Button(image=right_image, highlightthickness=0, command=remove_card)
right.grid(row=1, column=1)


next_card()







window.mainloop()
