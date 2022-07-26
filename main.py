import tkinter
import random
from pandas import read_csv
BACKGROUND_COLOR = "#B1DDC6"


window = tkinter.Tk()

data = read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


def randow_french_word():
    random_word = random.choice(to_learn)
    canvas.itemconfigure(
        word_canvas, text=random_word["French"], fill=BACKGROUND_COLOR)
    canvas.itemconfigure(title_canvas, text="French", fill=BACKGROUND_COLOR)
    canvas.itemconfig(french_image, image=my_image)
    window.after(ms=3000, func=change_image)


def change_image():
    random_word = random.choice(to_learn)
    # french_word =
    canvas.itemconfig(french_image, image=new_image)
    canvas.itemconfigure(
        word_canvas, text=random_word["French"], fill="#FFFFFF")
    canvas.itemconfigure(title_canvas, text="English", fill="#FFFFFF")


window.title("Flashy")
window.config(padx=50, pady=50)


window.config(background=BACKGROUND_COLOR)
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)

my_image = tkinter.PhotoImage(file="images/card_front.png")
french_image = canvas.create_image(400, 263, image=my_image)

new_image = tkinter.PhotoImage(file="images/card_back.png")

title_canvas = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))

word_canvas = canvas.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3, rowspan=2)


ok_logo = tkinter.PhotoImage(file="images/right.png")
button = tkinter.Button(
    image=ok_logo, highlightthickness=0,  command=randow_french_word)
button.grid(column=0, row=2)

wrong_logo = tkinter.PhotoImage(file="images/wrong.png")
button = tkinter.Button(
    image=wrong_logo, highlightthickness=0, command=randow_french_word)
button.grid(column=2, row=2)

randow_french_word()


window.mainloop()
