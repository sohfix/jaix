import os

import pygame

# Initialize Pygame
pygame.mixer.init()


def play_music(file_path):
    """
    Plays the music file specified by the file path.
    Supports .mp3 and .m4a file formats.
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    if not file_path.endswith(("", ".wav")):
        print("Unsupported file format. Please use .mp3 or .m4a")
        return

    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f"Playing: {file_path}")


def pause_music():
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


# Example usage
# play_music('path/to/your/musicfile.mp3')
# pause_music()
