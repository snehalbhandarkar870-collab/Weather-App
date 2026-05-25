# Import required libraries
import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def get_weather():
    
    # Get city name from input box
    city = city_entry.get()

    # Check if city is empty
    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    # Weather API URL
    url = f"https://wttr.in/{city}?format=3"

    try:
        # Send request to API
        response = requests.get(url)

        # Display weather result
        result_label.config(text=response.text)

    except:
        messagebox.showerror("Error", "Unable to fetch weather data")


# Create main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# Heading
title_label = tk.Label(root, text="Weather App", font=("Arial", 20))
title_label.pack(pady=10)

# City input box
city_entry = tk.Entry(root, width=30, font=("Arial", 14))
city_entry.pack(pady=10)

# Button
search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Run application
root.mainloop()