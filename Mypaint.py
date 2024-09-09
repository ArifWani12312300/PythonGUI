import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application")
        self.root.geometry("800x600")

        # Variables for paint settings
        self.brush_color = "black"
        self.brush_size = 5

        # Create and configure the canvas
        self.canvas = tk.Canvas(root, bg="white", width=800, height=500)
        self.canvas.pack(padx=10, pady=10)

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint)

        # Create control panel
        self.control_panel = tk.Frame(root)
        self.control_panel.pack()

        # Brush size slider
        self.size_slider = tk.Scale(self.control_panel, from_=1, to=20, orient="horizontal", label="Brush Size")
        self.size_slider.set(self.brush_size)
        self.size_slider.pack(side="left", padx=10)

        # Color picker button
        self.color_button = tk.Button(self.control_panel, text="Choose Color", command=self.choose_color)
        self.color_button.pack(side="left", padx=10)

        # Clear canvas button
        self.clear_button = tk.Button(self.control_panel, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack(side="left", padx=10)

    def choose_color(self):
        color_code = colorchooser.askcolor()[1]
        if color_code:
            self.brush_color = color_code

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        brush_size = self.size_slider.get()
        x1, y1 = (event.x - brush_size), (event.y - brush_size)
        x2, y2 = (event.x + brush_size), (event.y + brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

# Initialize the main window and start the application
root = tk.Tk()
app = PaintApp(root)
root.mainloop()
