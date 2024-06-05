import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        # Create the main interface elements
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 16))
        self.label.pack(pady=20)
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(pady=20)
        
        self.rock_button = tk.Button(self.buttons_frame, text="Rock", width=10, command=lambda: self.play("Rock"))
        self.rock_button.grid(row=0, column=0, padx=10)
        
        self.paper_button = tk.Button(self.buttons_frame, text="Paper", width=10, command=lambda: self.play("Paper"))
        self.paper_button.grid(row=0, column=1, padx=10)
        
        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", width=10, command=lambda: self.play("Scissors"))
        self.scissors_button.grid(row=0, column=2, padx=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)
        
        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)
        
        self.reset_button = tk.Button(root, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(pady=10)
        
        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
    
    def play(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == "Win":
            self.user_score += 1
            result_text = f"You chose {user_choice} and the computer chose {computer_choice}. You win!"
        elif result == "Lose":
            self.computer_score += 1
            result_text = f"You chose {user_choice} and the computer chose {computer_choice}. You lose!"
        else:
            result_text = f"You chose {user_choice} and the computer chose {computer_choice}. It's a tie!"
        
        self.result_label.config(text=result_text)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "Win"
        else:
            return "Lose"
    
    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.result_label.config(text="")
        self.score_label.config(text="Score - You: 0, Computer: 0")
        messagebox.showinfo("Game Reset", "The game has been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
