import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.master.geometry("400x300")
        self.user_score = 0
        self.computer_score = 0

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choose Rock, Paper, or Scissors:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self.master, text="Rock", command=lambda: self.play("Rock"), width=10)
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.master, text="Paper", command=lambda: self.play("Paper"), width=10)
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.master, text="Scissors", command=lambda: self.play("Scissors"), width=10)
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", font=('Arial', 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.master, text="User: 0  Computer: 0", font=('Arial', 12))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.reset_game, width=10)
        self.play_again_button.pack(pady=5)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.update_result(user_choice, computer_choice, result)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a Tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            self.user_score += 1
            return "You Win!"
        else:
            self.computer_score += 1
            return "You Lose!"

    def update_result(self, user_choice, computer_choice, result):
        self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}.\n{result}")
        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="User: 0  Computer: 0")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
