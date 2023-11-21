import tkinter as tk
from datetime import datetime
from tkinter import Checkbutton, IntVar, Label, Menu, Toplevel

from config import *
from music import pause_music, play_music

# todo: add a menu bar /    check some stuff
name = ""
BANNER = f"               Welcome to the JackPAI {name}!                 "
filepath = file_route


# Animation function for the banner
def animate_banner():
    text = banner_label.cget("text")
    banner_label.config(text=text[1:] + text[0])
    root.after(
        200, animate_banner
    )  # Adjust the speed of animation by changing the time here


# Define callback functions for each button
def obp_1(arg=1):
    pass


def obp_2():
    filepath = file_route('sohfix0')
    play_music(filepath)


def obp_3(arg=1):
    filepath = file_route
    pause_music(filepath)


def obp_4():
    pass


def obp_5():
    pass


def obp_6():
    pass


# Function to update the date and time display
def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_time)


# Create the main application window
root = tk.Tk()
root.title("JackPAI")
root.geometry("800x480")

# Create a banner label with animated text
banner_text = f" {BANNER} "
banner_label = Label(root, text=banner_text, font=("Arial", 18), bg="blue", fg="white")
banner_label.grid(sticky="ew", row=0, column=0)

# Start the banner animation
animate_banner()

# Create a frame for the buttons
frame = tk.Frame(root)
frame.grid(sticky="nsew", row=1, column=0)

# Configure the frame and root window to take up the grid properly
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

button_functions = [obp_1, obp_2, obp_3, obp_4, obp_5, obp_6]
for i in range(3):  # 3 columns wide
    frame.grid_columnconfigure(i, weight=1)
    for j in range(2):  # 2 rows long
        x = j * 3 + i + 1

        def sw(ar):
            switch_dict = {
                1: "Load Playlist",
                2: "Play/Pause",
                3: "Download Playlist",
                4: "xxx",
                5: "xxx",
                6: "xxx",
            }
            return switch_dict.get(ar, "Invalid option")

        frame.grid_rowconfigure(j, weight=1)
        button = tk.Button(
            frame,
            text=f"{sw(x)}",
            command=button_functions[j * 3 + i],
        )
        button.grid(row=j, column=i, sticky="nsew", padx=5, pady=5)

# Date and Time display in a digital clock style, positioned below the buttons
time_label = Label(root, font=("Consolas", 24, "bold"), bg="black", fg="yellow")
time_label.grid(sticky="nsew", row=2, column=0)
update_time()

# Start the Tkinter event loop
root.mainloop()
# Enable the X button to fucking work
root.quit()
