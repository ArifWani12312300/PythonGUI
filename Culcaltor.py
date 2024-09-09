import tkinter as tk

# Function to update the expression in the text entry
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Function to clear the text entry
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

# Function to calculate the result
def btn_equal():
    try:
        global expression
        result = str(eval(expression))  # Use eval to evaluate the expression
        input_text.set(result)
        expression = result  # Keep the result for further calculations
    except:
        input_text.set("Error")
        expression = ""

# Creating the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x400")
root.resizable(0, 0)
root.configure(bg="#2C3E50")  # Set background color

expression = ""

# StringVar to update the input field
input_text = tk.StringVar()

# Creating the input field
input_frame = tk.Frame(root,bg="#2C3E50")
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=22, justify='right')
input_field.grid(row=0, column=0)

# Creating the buttons frame
btns_frame = tk.Frame(root, bg="#2C3E50")
btns_frame.pack()

# Define button layout
buttons = [
    ('7', 1, 0, '#ECF0F1', '#2C3E50'), ('8', 1, 1, '#ECF0F1', '#2C3E50'), ('9', 1, 2, '#ECF0F1', '#2C3E50'), ('/', 1, 3, '#F39C12', '#2C3E50'),
    ('4', 2, 0, '#ECF0F1', '#2C3E50'), ('5', 2, 1, '#ECF0F1', '#2C3E50'), ('6', 2, 2, '#ECF0F1', '#2C3E50'), ('*', 2, 3, '#F39C12', '#2C3E50'),
    ('1', 3, 0, '#ECF0F1', '#2C3E50'), ('2', 3, 1, '#ECF0F1', '#2C3E50'), ('3', 3, 2, '#ECF0F1', '#2C3E50'), ('-', 3, 3, '#F39C12', '#2C3E50'),
    ('C', 4, 0, '#E74C3C', '#ECF0F1'), ('0', 4, 1, '#ECF0F1', '#2C3E50'), ('=', 4, 2, '#2ECC71', '#ECF0F1'), ('+', 4, 3, '#F39C12', '#2C3E50'),
]

# Loop to create buttons
for (text, row, col,fg,bg) in buttons:
    if text == 'C':
        btn = tk.Button(btns_frame, text=text, width=10, height=3, command=btn_clear)
    elif text == '=':
        btn = tk.Button(btns_frame, text=text, width=10, height=3, command=btn_equal)
    else:
        btn = tk.Button(btns_frame, text=text, width=10, height=3, command=lambda t=text: btn_click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
