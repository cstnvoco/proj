import tkinter as tk
from tkinter import ttk, messagebox
import random

red = (32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3)
black = (15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26)
green = (0,)
numbers = red + black + green

def get_color(number):
    if number in red:
        return "red"
    elif number in black:
        return "black"
    else:
        return "green"

def spin():
    chosen_color = color_choice.get()
    number_input = number_entry.get()

    if chosen_color not in ("red", "black", "green"):
        messagebox.showerror("Error", "Please select a valid color.")
        return

    try:
        if number_input:
            chosen_number = int(number_input)
            if chosen_number not in numbers:
                raise ValueError
        else:
            chosen_number = None
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number or leave it empty.")
        return

    spin_number = random.choice(numbers)
    spin_color = get_color(spin_number)

    result = f"Spin: {spin_color} {spin_number}"
    win = False

    if chosen_color == spin_color:
        win = True
    if chosen_number is not None and chosen_number == spin_number:
        win = True

    if win:
        result += "\n🎉 Voitsid!"
    else:
        result += "\n❌ Kaotasid."

    result_label.config(text=result)

root = tk.Tk()
root.title("Roulette Game")
root.geometry("300x250")
root.configure(bg="#2c2f33")

style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2c2f33", foreground="white")
style.configure("TButton", background="#7289da", foreground="white", padding=6)
style.configure("TCombobox", padding=4)

ttk.Label(root, text="Choose a color:").pack(pady=5)
color_choice = ttk.Combobox(root, values=["red", "black", "green"])
color_choice.pack()

ttk.Label(root, text="Choose a number (optional):").pack(pady=5)
number_entry = ttk.Entry(root)
number_entry.pack()

ttk.Button(root, text="Spin", command=spin).pack(pady=15)

result_label = ttk.Label(root, text="", font=("Arial", 12), justify="center", anchor="center")
result_label.pack(pady=10)

root.mainloop()
