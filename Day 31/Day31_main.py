# Day 31 Capstone Project - Flashcard App

import tkinter
from tkinter import messagebox
import pandas
import random

FONT1 = ("Arial", 18, "italic")
FONT2 = ("Arial", 34, "bold")
FONT3 = ("Arial", 20, "bold")
BGCOLOUR = "#B1DDC6"
current_card = ()
learned_words = []

window = tkinter.Tk()
window.title("Flashcard App")
window.config(padx=50, pady=50, bg=BGCOLOUR)

try:
    words_df = pandas.read_csv("./data/learned_words.csv")
except FileNotFoundError:
    words_df = pandas.read_csv("./data/french_words.csv")


def french_card(card, words):
    """Changes the current display to the French side"""
    global card_side
    word_fr = words.French[card]
    card_canvas.itemconfig(card_image, image=card_front_img)
    card_canvas.itemconfig(card_title, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=word_fr, fill="black")
    card_side = 0


def english_card(card, words):
    """Changes the current display to the English side"""
    global card_side
    word_en = words.English[card]
    card_canvas.itemconfig(card_image, image=card_back_img)
    card_canvas.itemconfig(card_title, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=word_en, fill="white")
    card_side = 1


def generate_card():
    """Generates a random card from the French words csv file"""
    global current_card
    current_card = random.randint(0, len(words_df)-1)
    if current_card not in learned_words:
        french_card(current_card, words_df)
    else:
        generate_card()


def flip_card():
    """Flips the card between the English and French side"""
    global card_side
    if card_side == 0:
        english_card(current_card, words_df)
    elif card_side == 1:
        french_card(current_card, words_df)


def learned_card():
    global words_df
    learned_words.append(current_card)
    num_cards_label.config(text=f"Learned: {len(learned_words)}")
    try:
        generate_card()
    except RecursionError:
        num_cards_label.config(text="You learned all the words!", fg="green")
        right_button.config(state="disabled")
        wrong_button.config(state="disabled")


def save_file():
    answer = messagebox.askyesno(title="Flashcard App Closing", message="Would you like to save your learned words?")
    if answer:
        words_df.drop(labels=learned_words).to_csv("./data/learned_words.csv", index=False)

    window.destroy()


# ---------- Cards ---------- #
card_canvas = tkinter.Canvas(width=400, height=263, highlightthickness=0, bg=BGCOLOUR)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png").subsample(2, 2)
card_back_img = tkinter.PhotoImage(file="./images/card_back.png").subsample(2, 2)
card_image = card_canvas.create_image(200, 132, image=card_front_img)
card_side = 0
card_title = card_canvas.create_text(200, 75, text="Language", font=FONT1)
card_word = card_canvas.create_text(200, 132, text="Word", font=FONT2)
card_canvas.grid(column=0, row=0, columnspan=2)

# ---------- Right Button ---------- #
right_img = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0, borderwidth=0, command=learned_card)
right_button.grid(column=1, row=1)

# ---------- Wrong Button ---------- #
wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=generate_card)
wrong_button.grid(column=0, row=1)

# ---------- Flip Button ---------- #
flip_img = tkinter.PhotoImage(file="./images/flip3.png").subsample(3, 3)
flip_button = tkinter.Button(image=flip_img, highlightthickness=0, borderwidth=0, command=flip_card, fg=BGCOLOUR)
flip_button.grid(column=2, row=0)

# ---------- Cards Learned Label ---------- #
num_cards_label = tkinter.Label(text="Learned: 0", bg=BGCOLOUR, fg="blue", font=FONT3)
num_cards_label.grid(column=0, row=2, columnspan=2)

generate_card()

window.protocol("WM_DELETE_WINDOW", save_file)
window.mainloop()
