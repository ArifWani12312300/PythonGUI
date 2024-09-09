import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Set player to 'X' initially
current_player = "X"
buttons = []

# Function to check if a player has won
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# Function to check if the board is full (i.e., a tie)
def check_tie():
    for row in buttons:
        for button in row:
            if button["text"] == "":
                return False
    return True

# Function to handle button clicks
def on_button_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not check_winner():
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_tie():
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_board()
        else:
            # Switch player
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game board
def reset_board():
    global current_player
    current_player = "X"
    for row in buttons:
        for button in row:
            button["text"] = ""

# Create the 3x3 grid of buttons
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=row, c=col: on_button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Start the main event loop
root.mainloop()
