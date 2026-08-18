import random as ran
import tkinter as tk
from data import random_mob

def get_player_count():
    player_count = int(entry_box.get())

    players = []

    for i in range(player_count):
        players.append(i)

    morphs = []

    for each in players:
        variant = ran.choice(random_mob())
        morphs.append((variant))


    question.destroy()
    entry_box.destroy()
    enter.destroy()

    for each in players:
        label = tk.Entry(root, textvariable=tk.StringVar(value=f"Player {each+1}: {morphs[each]}"), state="readonly", bd=0, fg="white",readonlybackground=root.cget("bg"), font=("Arial", 12))
        label.pack(pady=5, fill="x")

    root.update_idletasks()

root = tk.Tk()
root.title("Mob Randomizer")
root.geometry("400x300")

question = tk.Label(root, text="How many players are there?")
question.pack(pady=10)
entry_box = tk.Entry(root, width=30)
entry_box.pack(pady=10)
enter = tk.Button(root, text="Enter", command=lambda: get_player_count())
enter.pack(pady=10)

root.mainloop()