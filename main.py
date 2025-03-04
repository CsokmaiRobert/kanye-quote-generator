from tkinter import *
import requests


def get_quote():
    request = requests.get("https://api.kanye.rest")
    request.raise_for_status()
    quote = request.json()["quote"]
    canvas.itemconfig(quote_text, text=f"{quote}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

first_request = requests.get("https://api.kanye.rest")
first_request.raise_for_status()
first_quote = first_request.json()["quote"]

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=f"{first_quote}", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()