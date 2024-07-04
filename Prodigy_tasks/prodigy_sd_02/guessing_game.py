import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        self.master.configure(bg="#ffe4e1")  #pastel rose bg 

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        #title label
        self.title_label = tk.Label(master, text="Number Guessing Game", font=("Helvetica", 16, "bold"), bg="#ffe4e1", fg="#8b4513")  # Chocolate text color
        self.title_label.pack(pady=10)

        #instruction label
        self.label = tk.Label(master, text="Guess a number between 1 and 100:", font=("Helvetica", 12), bg="#ffe4e1", fg="#8b4513")  # Saddle Brown text color
        self.label.pack(pady=5)

        #entry widget
        self.entry = tk.Entry(master, font=("Helvetica", 12), bg="#faf0e6", fg="#8b4513")  # Linen background, Saddle Brown text color
        self.entry.pack(pady=5)

        #guess button 
        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess, font=("Helvetica", 12), bg="#ffb6c1", fg="white")  # Light Pink background, white text
        self.guess_button.pack(pady=10)

        #this is a feedback label
        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#ffe4e1", fg="#8b4513")  # Saddle Brown text color
        self.feedback_label.pack(pady=5)

    def check_guess(self):
        try:
            user_guess = int(self.entry.get())
            self.attempts += 1

            if user_guess < self.number_to_guess:
                self.feedback_label.config(text="Too low! Try again.", fg="#dc143c")  # Crimson text color
            elif user_guess > self.number_to_guess:
                self.feedback_label.config(text="Too high! Try again.", fg="#dc143c")  # Crimson text color
            else:
                messagebox.showinfo("Congratulations!", f"Correct! You guessed the number in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Invalid input! Please enter an integer.", fg="#ff0000")  # Red text

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
