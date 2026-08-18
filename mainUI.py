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


    question.pack_forget()
    entry_box.pack_forget()
    enter.pack_forget()

    for each in players:
        label = tk.Entry(root, textvariable=tk.StringVar(value=morphs[each]), state="readonly", bd=0, fg="#FFFFFF",readonlybackground=root.cget("bg"), font=("Arial", 12))
        label.pack(pady=5, fill="x")

    done = tk.Button(root, text="Done", command=lambda: run())
    done.pack(pady=10)

    root.update_idletasks()

def run():
    global question, entry_box, enter
    for each in root.winfo_children():
        if each not in [question, entry_box, enter]:
            each.destroy()
    question = tk.Label(root, text="How many players are there?")
    question.pack(pady=10)
    entry_box = tk.Entry(root, width=30)
    entry_box.pack(pady=10)
    enter = tk.Button(root, text="Enter", command=lambda: get_player_count())
    enter.pack(pady=10)
    root.update_idletasks()

root = tk.Tk()
root.title("Mob Randomizer")
root.geometry("400x300")
root.configure(bg="#343434")

question = tk.Label(root, text="How many players are there?")
question.pack(pady=10)
entry_box = tk.Entry(root, width=30)
entry_box.pack(pady=10)
enter = tk.Button(root, text="Enter", command=lambda: get_player_count())
enter.pack(pady=10)

root.mainloop()