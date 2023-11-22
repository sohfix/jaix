#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import random
import tkinter as tk
from datetime import datetime
from tkinter import Label

import pygame
import pyttsx3
import requests
# Assuming 'config.py' exists with necessary configurations
from config import *

# Initialize Pygame for music playback
pygame.mixer.init()

# Main application window using Tkinter
root = tk.Tk()
root.title("JackPAI")
root.geometry("800x480")


# Function to animate the banner text
def animate_banner():
    text = banner_label.cget("text")
    banner_label.config(text=text[1:] + text[0])
    root.after(200, animate_banner)


# Function to update the date and time display
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)


# Define callback functions for buttons
def obp_1():
    resume()


def obp_2():
    play(file_route("sohfix0"))


def obp_3():
    pause()


def obp_4():
    speak_weather()


def obp_5():
    pass  # Extend as needed


def obp_6():
    pass  # Extend as needed


# Function to speak the weather data
def speak_weather():
    apikey = "2980efa1d58e8dc13a69236bb16f37da"
    data = get_weather_data("chicago", apikey)
    speaker = pyttsx3.init()
    for line in data:
        speaker.say(line)
    speaker.runAndWait()


# Function to fetch weather data
def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [
            f"Temperature: {data['main']['temp']}°C",
            f"Wind Speed: {data['wind']['speed']} km/h",
            f"Wind Direction: {data['wind']['deg']}°",
        ]
    else:
        return ["Error fetching data"]


# Function to determine file route for music
def file_route(user="sohfix"):
    random_number = random.randint(1, 32)
    return f"/home/{user}/Music/{random_number}"


# Functions for music playback control
def play(fs):
    if not os.path.exists(fs):
        return
    pygame.mixer.music.load(fs)
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def resume():
    pygame.mixer.music.unpause()


# Create UI components
banner_label = Label(
    root, text=" Welcome to JackPAI! ", font=("Arial", 18), bg="blue", fg="white"
)
banner_label.grid(sticky="ew", row=0, column=0)
animate_banner()

frame = tk.Frame(root)
frame.grid(sticky="nsew", row=1, column=0)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

button_functions = [obp_1, obp_2, obp_3, obp_4, obp_5, obp_6]
button_texts = [
    "Resume",
    "Play/Shuffle",
    "Pause",
    "Weather Report",
    "Option 5",
    "Option 6",
]

for i in range(3):
    frame.grid_columnconfigure(i, weight=1)
    for j in range(2):
        frame.grid_rowconfigure(j, weight=1)
        button = tk.Button(
            frame, text=button_texts[j * 3 + i], command=button_functions[j * 3 + i]
        )
        button.grid(row=j, column=i, sticky="nsew", padx=5, pady=5)

time_label = Label(root, font=("Consolas", 24, "bold"), bg="black", fg="yellow")
time_label.grid(sticky="nsew", row=2, column=0)
update_time()

root.mainloop()
