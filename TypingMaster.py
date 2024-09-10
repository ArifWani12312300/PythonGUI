import tkinter as tk
from tkinter import messagebox
import time
import random

# Sample paragraphs to type
paragraphs = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language for beginners.",
    "Machine learning is fascinating and fun to learn.",
    "Data science is the future of modern technologies.",
    "Artificial intelligence will shape the world in the coming decades."
]

class TypingMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Master")
        self.root.geometry("800x600")

        self.time_start = 0
        self.time_end = 0
        self.time_limit = 60  # Time limit in seconds
        self.timer_running = False

        self.text_to_type = random.choice(paragraphs)
        self.typed_text = ""

        # Create labels, text areas, and buttons
        self.label1 = tk.Label(root, text="Type the following paragraph:", font=("Helvetica", 14))
        self.label1.pack(pady=10)

        self.text_display = tk.Text(root, height=5, width=80, wrap="word", font=("Helvetica", 12))
        self.text_display.pack(pady=10)
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state=tk.DISABLED)

        self.label2 = tk.Label(root, text="Start typing below:", font=("Helvetica", 14))
        self.label2.pack(pady=10)

        self.text_input = tk.Text(root, height=5, width=80, wrap="word", font=("Helvetica", 12))
        self.text_input.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing, font=("Helvetica", 12), bg="green", fg="white")
        self.start_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_typing, font=("Helvetica", 12), bg="red", fg="white")
        self.reset_button.pack(pady=5)

        self.timer_label = tk.Label(root, text="Time left: 60", font=("Helvetica", 14), fg="blue")
        self.timer_label.pack(pady=10)

        self.results_label = tk.Label(root, text="", font=("Helvetica", 14), fg="blue")
        self.results_label.pack(pady=10)

        self.accuracy_scoreboard = tk.Label(root, text="Accuracy Scoreboard", font=("Helvetica", 14))
        self.accuracy_scoreboard.pack(pady=10)

        self.accuracy_listbox = tk.Listbox(root, height=5, width=50, font=("Helvetica", 12))
        self.accuracy_listbox.pack(pady=10)

    def start_typing(self):
        if not self.timer_running:
            self.time_start = time.time()
            self.timer_running = True
            self.update_timer()
            self.text_input.bind("<KeyRelease>", self.on_key_release)
            self.text_input.focus()

    def on_key_release(self, event):
        if self.text_input.get("1.0", tk.END).strip() == self.text_to_type.strip():
            self.time_end = time.time()
            self.calculate_results()

    def update_timer(self):
        elapsed_time = time.time() - self.time_start
        remaining_time = self.time_limit - int(elapsed_time)

        if remaining_time <= 0:
            self.timer_label.config(text="Time's up!")
            self.calculate_results()
        else:
            self.timer_label.config(text=f"Time left: {remaining_time}")
            self.root.after(1000, self.update_timer)

    def calculate_results(self):
        self.timer_running = False
        self.time_end = time.time()
        total_time = self.time_end - self.time_start
        minutes = total_time / 60

        # Calculate words per minute (WPM)
        words = len(self.typed_text.split())
        wpm = words / minutes

        # Calculate accuracy
        correct_chars = 0
        for typed_char, original_char in zip(self.typed_text, self.text_to_type):
            if typed_char == original_char:
                correct_chars += 1
        accuracy = (correct_chars / len(self.text_to_type)) * 100

        # Update the scoreboard
        self.accuracy_listbox.insert(tk.END, f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")

        # Show the results
        self.results_label.config(text=f"Speed: {wpm:.2f} WPM | Accuracy: {accuracy:.2f}%")

    def reset_typing(self):
        # Reset all fields for a new test
        self.time_start = 0
        self.time_end = 0
        self.typed_text = ""
        self.timer_running = False

        self.text_to_type = random.choice(paragraphs)
        self.text_display.config(state=tk.NORMAL)
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, self.text_to_type)
        self.text_display.config(state=tk.DISABLED)

        self.text_input.delete("1.0", tk.END)
        self.results_label.config(text="")
        self.timer_label.config(text=f"Time left: {self.time_limit}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingMaster(root)
    root.mainloop()
