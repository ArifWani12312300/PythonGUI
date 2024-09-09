import tkinter as tk
from tkinter import messagebox

# Hardcoded username and password for demo purposes
USER_CREDENTIALS = {
    'username': 'admin',
    'password': 'password123'
}

# Function to validate the login
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the username and password are correct
    if entered_username == USER_CREDENTIALS['username'] and entered_password == USER_CREDENTIALS['password']:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.quit()  # Closes the window
    else: 
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Main application window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")  # Set window size

# Create and place widgets
tk.Label(root, text="Username").pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

tk.Label(root, text="Password").pack(pady=10)
password_entry = tk.Entry(root, show='*')  # Password hidden with '*'
password_entry.pack(pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Start the main event loop
root.mainloop()
