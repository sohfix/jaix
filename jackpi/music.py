import os

import pygame
from config import *

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
        print(
            f"Unsupported file format. {fs[:-4]} not supported. Supported formats: ALL"
        )
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


def resume():
    """
    Resumes the currently paused music.
    """
    if not pygame.mixer.music.get_busy():
        if pygame.mixer.music.get_pos() >= 0:
            pygame.mixer.music.unpause()
            print("Music resumed.")
        else:
            print("Music is not paused.")
    else:
        print("No music is playing.")
