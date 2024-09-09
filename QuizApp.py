import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["Shakespeare", "Hemingway", "Poe", "Twain"],
        "answer": "Shakespeare"
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["H2O", "O2", "CO2", "NaCl"],
        "answer": "H2O"
    },
]

# Shuffle questions for randomness
random.shuffle(quiz_data)

# Global variables
current_question = 0
score = 0
time_left = 10  # 10 seconds for each question

# Function to start the timer
def start_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Time left: {time_left}s")
        root.after(1000, start_timer)  # Call this function every 1 second
    else:
        check_answer()  # Automatically submit the answer when time runs out

# Function to load the next question
def load_question():
    global current_question, time_left
    if current_question < len(quiz_data):
        time_left = 10  # Reset the timer
        start_timer()  # Start the timer
        question_data = quiz_data[current_question]
        question_label.config(text=question_data["question"])

        # Display choices
        for idx, choice in enumerate(question_data["choices"]):
            choices_radio_buttons[idx].config(text=choice, value=choice)
    else:
        show_score()

# Function to check the selected answer
def check_answer():
    global current_question, score
    selected_answer = selected_choice.get()
    if selected_answer == quiz_data[current_question]["answer"]:
        score += 1
    current_question += 1
    load_question()

# Function to show the final score
def show_score():
    messagebox.showinfo("Quiz Completed", f"Your final score is: {score}/{len(quiz_data)}")
    root.quit()  # Exit the app

# Main app window
root = tk.Tk()
root.title("Advanced Quiz App")
root.geometry("500x400")
root.config(bg="lightblue")

# Question label
question_label = tk.Label(root, text="", font=("Helvetica", 16), bg="lightblue", wraplength=400)
question_label.pack(pady=20)

# Timer label
timer_label = tk.Label(root, text=f"Time left: {time_left}s", font=("Helvetica", 14), bg="lightblue")
timer_label.pack(pady=10)

# Variable to track the selected answer
selected_choice = tk.StringVar()

# Radio buttons for multiple-choice answers
choices_radio_buttons = []
for i in range(4):  # Assuming each question has 4 choices
    radio_btn = tk.Radiobutton(root, text="", variable=selected_choice, value="", font=("Helvetica", 14), bg="lightblue")
    radio_btn.pack(anchor="w", padx=20, pady=5)
    choices_radio_buttons.append(radio_btn)

# Next button to submit answer and go to the next question
next_button = tk.Button(root, text="Submit Answer", command=check_answer, font=("Helvetica", 14), bg="green", fg="white")
next_button.pack(pady=20)

# Load the first question
load_question()

# Start the Tkinter main loop
root.mainloop()
