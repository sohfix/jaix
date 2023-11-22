import os

import pyttsx3


class tts:
    """
    A Text to Speech class using pyttsx3. This class is optimized for use in
    environments with limited resources, such as a Raspberry Pi.
    """

    def __init__(self):
        """
        Initializes the Text to Speech engine.
        pyttsx3.init() can be resource-intensive, so ensure this is called sparingly.
        """
        self.engine = pyttsx3.init()

    def Speak(self, text: list) -> None:
        """
        Speaks out the text provided in the list.

        Args:
            text (list): A list of strings to be spoken.

        Raises:
            TypeError: If the provided text is not a list.
        """
        if not isinstance(text, list):
            raise TypeError("Must be a list.")

        for t in text:
            self.engine.say(t)
            # Run the engine for each phrase to avoid queuing too many in memory
            self.engine.runAndWait()

    def Save(self, message: str, file_name: str) -> None:
        """
        Saves the spoken message to an MP3 file.

        Args:
            message (str): The message to be converted to speech.
            file_name (str): The name of the file to save the speech.

        Raises:
            TypeError: If message or file_name is not a string.
        """
        if not isinstance(message, str) or not isinstance(file_name, str):
            raise TypeError("Both message and file_name must be strings.")

        # Construct the file path in a platform-independent way
        base_dir = "/home/sohfix0/Documents/temps/"
        file_path = os.path.join(base_dir, f"{file_name}.mp3")

        # Save the speech to a file
        self.engine.save_to_file(message, file_path)
        self.engine.runAndWait()


# Example usage of the TextToSpeech class
if __name__ == "__main__":
    tts = TextToSpeech()
    tts.Speak(["Hello", "This is a test message"])
    tts.Save("This will be saved as an audio file.", "test_audio")
