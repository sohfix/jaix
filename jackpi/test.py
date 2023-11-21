import os

import JackTube
import JackUtilities
from JackUtilities import Banner as JackBanner
from JackUtilities import TextToSpeech
from printy import inputy, printy


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    printy("Good day.", "y")
