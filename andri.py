import tkinter as tk
import random

def start_race():
    racers = []
    for i in range(num_racers.get()):
        racers.append(random.uniform(20, 30))

    winner = min(racers)
    winner_index = racers.index(winner)
    result_label.config(text="Racer " + str(winner_index + 1) + " wins with time: " + str(winner))

app = tk.Tk()
app.title("Race Simulator")

num_racers = tk.IntVar()
racers_entry = tk.Entry(app, textvariable=num_racers)
racers_entry.pack()

start_button = tk.Button(app, text="Start Race", command=start_race)
start_button.pack()

result_label = tk.Label(app)
result_label.pack()

app.mainloop()
