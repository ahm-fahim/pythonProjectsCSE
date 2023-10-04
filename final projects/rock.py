import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors Game")
        self.user_wins = 0
        self.computer_wins = 0
        self.rounds = 0

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.rock_button = tk.Button(self.frame, text="Rock", width=10, command=lambda: self.play_game("rock"))
        self.paper_button = tk.Button(self.frame, text="Paper", width=10, command=lambda: self.play_game("paper"))
        self.scissors_button = tk.Button(self.frame, text="Scissors", width=10, command=lambda: self.play_game("scissors"))

        self.rock_button.pack(side=tk.LEFT)
        self.paper_button.pack(side=tk.LEFT)
        self.scissors_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(self.root, text="Quit", width=10, command=self.show_results)
        self.quit_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

    def play_game(self, user_choice):
        self.rounds += 1
        computer_choice = random.choice(["rock", "paper", "scissors"])

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            self.user_wins += 1
        else:
            result = "Computer wins!"
            self.computer_wins += 1

        self.result_label.config(text=f"Round {self.rounds}: Computer chose {computer_choice}. {result}")

    # RESULT 
    def show_results(self):
        if self.rounds == 0:
            messagebox.showinfo("Results", "No rounds played.")
        else:
            final_result = f"Final Results:\nYou won {self.user_wins} times.\nComputer won {self.computer_wins} times."
            messagebox.showinfo("Results", final_result)
        self.root.destroy()

#  start the main GUI 
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

