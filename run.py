import random
import tkinter as tk
from tkinter import ttk


TOWNS = ["bratislava", "kosice", "presov", "nitra", "zilina", "levice", "trnava", "trencin", "poprad", "kezmarok", "trebisov", "michalovce", "malacky", "levoca"]

def open_assignment():
    TOWNS.sort(reverse=True)

    window = tk.Toplevel(root)
    window.title("PT_Hornak")
    label = ttk.Label(window, text="Riešenie Úlohy", font=("Helvetica", 16))
    label.pack(pady=20, padx=20)

    town_label = ttk.Label(window, text=f"Mesta:\n {', '.join(TOWNS)}", font=("Helvetica", 12))
    town_label.pack(pady=10)

    first_fifth_tenth_label = ttk.Label(window, text=f"Prve Mesto: {TOWNS[0]}\nPiate Mesto: {TOWNS[4]}\nDesiate Mesto: {TOWNS[9]}", font=("Helvetica", 12))
    first_fifth_tenth_label.pack(pady=10)

    capitalized_town = [town.capitalize() for town in TOWNS]
    capitalized_town_label = ttk.Label(window, text=f"Mesta s velkým písmenom:\n {', '.join(capitalized_town)}", font=("Helvetica", 12))
    capitalized_town_label.pack(pady=10)

    random.shuffle(capitalized_town)
    random_towns = [f"{i+1}. {town}" for i, town in enumerate(capitalized_town)]
    random_towns_label = ttk.Label(window, text=f"Nahodne usporiadane mesta:\n {', '.join(random_towns)}", font=("Helvetica", 12))
    random_towns_label.pack(pady=10)



root = tk.Tk()
root.title("Programocacie Techniky")

title_label = ttk.Label(root, text="Programocacie Techniky", font=("Helvetica", 16))
title_label.pack(pady=10)

author_label = ttk.Label(root, text="Marián Horňák", font=("Helvetica", 12))
author_label.pack(pady=5)

assignment_label = ttk.Label(root, text="Zadanie úlohy:\n 6.  Vytvorte pole 14 mien miest z malých písmen (manuálne),\n zoraďte ich podľa abecedy zostupne, vypíšte prvé, piate a 10 meno,\n zmeňte všetky prvé písmená na veľké a vypíšte náhodný zoznam aj poradovými číslami.", font=("Helvetica", 12))
assignment_label.pack(pady=5)

start_button = ttk.Button(root, text="Start", command=open_assignment)
start_button.pack(pady=20)

root.mainloop()