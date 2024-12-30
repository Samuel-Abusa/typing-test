from tkinter import *
from random import randint
from texts import paragraphs
from funcs import HelperFuncs

RED = "#e7305b"

window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

timmer_label = Label(text="01:00", font=("Arial", 15), fg=RED)
timmer_label.pack()

text_widget = Text(window, height=20, width=145)
text_widget.pack(pady=20, padx=50)
text_widget.tag_configure(
    "fancy_font", font=("Arial", 14), justify="center", spacing1=5, spacing2=5
)

paragraph = paragraphs[randint(1, 10)]

text_widget.insert(END, paragraph, "fancy_font")

typing_field = Entry(window, width=100, font=("Arial", 15), justify="center")
typing_field.pack()


def render_labels(typed_words, correct_words, typos):
    speed_label = Label(
        text=f"Typing Speed {typed_words} WPM with {typos} typo{'' if typos == 1 else 's'} your net speed {correct_words}"
    )
    speed_label.pack()


func = HelperFuncs()

window.bind(
    "<Key>",
    lambda e: func.start_timer(
        60,
        timmer_label,
        window,
        [timmer_label, text_widget, typing_field],
        paragraph,
        render_labels,
    ),
)

window.mainloop()
