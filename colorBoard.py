import tkinter as tk
import random

# Function to generate a random color in hex format
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Function to change the color of a square when clicked
def change_color(event):
    event.widget.config(bg=random_color())

# Main application window
root = tk.Tk()
root.title("Color Board")
root.geometry("400x400")  # Set window size

# Number of rows and columns
rows, cols = 8, 8
cell_size = 50  # Size of each cell

# Create a grid of color squares
for row in range(rows):
    for col in range(cols):
        square = tk.Label(root, bg=random_color(), width=10, height=5, relief="raised", borderwidth=2)
        square.grid(row=row, column=col, padx=1, pady=1)
        square.bind("<Button-1>", change_color)  # Bind left-click to change color

# Run the application
root.mainloop()
