import requests
from tkinter import *

# ---------------- API FUNCTION ---------------- #
def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    quote_label.config(text=quote)

# ---------------- UI SETUP ---------------- #
window = Tk()
window.title("Kanye Says")
window.config(padx=40, pady=40)

quote_label = Label(
    text="Click the button to get a Kanye quote",
    wraplength=400,
    justify="center",
    font=("Arial", 14)
)
quote_label.pack(pady=20)

get_quote_button = Button(
    text="Get Quote",
    command=get_quote
)
get_quote_button.pack()

window.mainloop()
