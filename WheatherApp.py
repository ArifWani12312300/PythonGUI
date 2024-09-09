import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk  # For image handling

# Replace with your own OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
API_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'

# Function to get weather data
def get_weather(city):
    try:
        response = requests.get("b1b15e88fa797225412429c1c50c122a1>api.openweathermap.org/data/2.5/forecast?id&appid={API key}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        return None

# Function to display the weather information
def show_weather():
    city = city_entry.get()
    weather_data = get_weather(city)
    
    if weather_data:
        temp = weather_data['main']['temp']
        weather_desc = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        temp_label.config(text=f"Temperature: {temp}°C")
        desc_label.config(text=f"Condition: {weather_desc.capitalize()}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
        
        # Update the weather icon
        icon_code = weather_data['weather'][0]['icon']
        update_weather_icon(icon_code)
    else:
        messagebox.showerror("Error", "City not found! Please try again.")

# Function to update the weather icon
def update_weather_icon(icon_code):
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
    icon_response = requests.get(icon_url, stream=True)
    icon_data = Image.open(icon_response.raw)
    icon_data = icon_data.resize((100, 100), Image.ANTIALIAS)
    weather_icon = ImageTk.PhotoImage(icon_data)
    icon_label.config(image=weather_icon)
    icon_label.image = weather_icon  # Keep a reference to avoid garbage collection

# Main app window
root = tk.Tk()
root.title("Advanced Weather App")
root.geometry("400x500")
root.config(bg="#ADD8E6")  # Light blue background

# City entry
city_label = tk.Label(root, text="Enter City Name:", font=("Helvetica", 12), bg="#ADD8E6")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
city_entry.pack(pady=10)

# Search button
search_button = tk.Button(root, text="Search Weather", command=show_weather, font=("Helvetica", 12), bg="green", fg="white")
search_button.pack(pady=10)

# Weather information display
weather_frame = tk.Frame(root, bg="#ADD8E6")
weather_frame.pack(pady=20)

# Temperature label
temp_label = tk.Label(weather_frame, text="Temperature: --°C", font=("Helvetica", 16), bg="#ADD8E6")
temp_label.pack(pady=10)

# Description label
desc_label = tk.Label(weather_frame, text="Condition: --", font=("Helvetica", 16), bg="#ADD8E6")
desc_label.pack(pady=10)

# Humidity label
humidity_label = tk.Label(weather_frame, text="Humidity: --%", font=("Helvetica", 16), bg="#ADD8E6")
humidity_label.pack(pady=10)

# Wind speed label
wind_label = tk.Label(weather_frame, text="Wind Speed: -- m/s", font=("Helvetica", 16), bg="#ADD8E6")
wind_label.pack(pady=10)

# Weather icon
icon_label = tk.Label(weather_frame, bg="#ADD8E6")
icon_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
