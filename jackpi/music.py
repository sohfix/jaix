import os
import random
import pygame


def shuffle(directory="/home/sohfix0/Music/"):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Get a list of all audio files in the directory
    files = [f for f in os.listdir(directory) if f.endswith(".wav")]
    if not files:
        print("No audio files found in the directory.")
        return

    # Play the files in a random order
    while True:
        random_file = random.choice(files)
        print(f"Playing: {random_file}")
        pygame.mixer.music.load(os.path.join(directory, random_file))
        pygame.mixer.music.play()

        # Wait for the music to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


class MusicPlayer:
    def __init__(self, directory):
        self.directory = directory
        self.files = [f for f in os.listdir(directory) if f.endswith(".mp3")]
        self.current_track = None
        self.paused = False

        if not self.files:
            raise ValueError("No audio files found in the directory.")

        pygame.mixer.init()
        self.load_random_track()

    def load_random_track(self):
        self.current_track = random.choice(self.files)
        pygame.mixer.music.load(os.path.join(self.directory, self.current_track))

    def play_pause(self):
        if pygame.mixer.music.get_busy():
            # If music is playing or paused
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                print(f"Resumed: {self.current_track}")
            else:
                pygame.mixer.music.pause()
                self.paused = True
                print(f"Paused: {self.current_track}")
        else:
            # If music is not playing, start a new track
            self.load_random_track()
            pygame.mixer.music.play()
            print(f"Playing: {self.current_track}")

    def next_track(self):
        self.load_random_track()
        pygame.mixer.music.play()
        print(f"Playing: {self.current_track}")