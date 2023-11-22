import os
from config import *
import pygame

# Initialize Pygame
pygame.mixer.init()


def play(fs):
    """
    Plays the music file specified by the file path.
    Supports .mp3 and .m4a file formats.
    """
    if not os.path.exists(fs):
        print(f"File not found: {fs}")
        return

    if not fs.endswith(("", ".wav")):
        print("Unsupported file format. Please use .mp3 or .m4a")
        return

    pygame.mixer.music.load(fs)
    pygame.mixer.music.play()
    print(f"Playing: {fs}")


def pause():
    """
    Pauses the currently playing music. If the music is already paused, it will unpause it.
    """
    if pygame.mixer.music.get_busy():
        if pygame.mixer.music.get_pos() >= 0:
            pygame.mixer.music.pause()
            print("Music paused.")
        else:
            pygame.mixer.music.unpause()
            print("Music unpaused.")
    else:
        print("No music is playing.")
