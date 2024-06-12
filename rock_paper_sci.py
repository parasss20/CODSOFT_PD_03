import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0

        # Creating GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Label for user instructions
        self.instruction_label = ttk.Label(self.master, text="Choose Rock, Paper, or Scissors:")
        self.instruction_label.grid(row=0, columnspan=3, padx=10, pady=10)

        # Buttons for user choices
        self.rock_button = ttk.Button(self.master, text="Rock", command=lambda: self.play_game("Rock"))
        self.rock_button.grid(row=1, column=0, padx=5, pady=5)

        self.paper_button = ttk.Button(self.master, text="Paper", command=lambda: self.play_game("Paper"))
        self.paper_button.grid(row=1, column=1, padx=5, pady=5)

        self.scissors_button = ttk.Button(self.master, text="Scissors", command=lambda: self.play_game("Scissors"))
        self.scissors_button.grid(row=1, column=2, padx=5, pady=5)

        # Label to display user and computer choices
        self.choice_label = ttk.Label(self.master, text="")
        self.choice_label.grid(row=2, columnspan=3, padx=5, pady=5)

        # Label to display game result
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=3, columnspan=3, padx=5, pady=5)

        # Label to display scores
        self.score_label = ttk.Label(self.master, text="Score: User - 0, Computer - 0")
        self.score_label.grid(row=4, columnspan=3, padx=5, pady=5)

    def play_game(self, user_choice):
        # Generate computer choice
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        # Display user and computer choices
        self.choice_label.config(text=f"User choice: {user_choice}, Computer choice: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update score labels
        self.score_label.config(text=f"Score: User - {self.user_score}, Computer - {self.computer_score}")

        # Display game result
        self.result_label.config(text=result)

def main():
    root = tk.Tk()
    rps_game = RockPaperScissors(root)
    root.mainloop()

if __name__ == "__main__":
    main()
