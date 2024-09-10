import tkinter as tk
from tkinter import filedialog
import pygame
import os

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("600x400")

        # Initialize Pygame for video playback
        pygame.init()
        pygame.display.set_mode((640, 480))

        # Create the GUI elements
        self.label = tk.Label(root, text="Choose a video file to play", font=("Arial", 18))
        self.label.pack(pady=20)

        self.play_button = tk.Button(root, text="Play Video", command=self.play_video)
        self.play_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Video", command=self.stop_video)
        self.stop_button.pack(pady=10)

    def play_video(self):
        video_file = filedialog.askopenfilename(title="Select Video File", filetypes=(("MP4 files", "*.mp4"), ("All files", "*.*")))
        
        if video_file:
            self.label.config(text=f"Now Playing: {os.path.basename(video_file)}")
            
            # Load and play the video using Pygame
            pygame.display.set_caption(os.path.basename(video_file))
            pygame.movie = pygame.movie.Movie(video_file)
            screen = pygame.display.get_surface()

            # Play the video
            pygame.movie.set_display(screen)
            pygame.movie.play()

    def stop_video(self):
        if pygame.movie.get_busy():
            pygame.movie.stop()
            self.label.config(text="Video Stopped")

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
