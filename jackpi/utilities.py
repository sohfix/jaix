import os

import pyttsx3
from printy import inputy, printy
from pyfiglet import Figlet


class Error:
    @staticmethod
    def RaiseTypeError(
        var: object,
        typed: object,
    ) -> None:
        if not isinstance(var, typed):
            raise TypeError(f"Parameter must be of type {type(typed)}")
        return None

    @staticmethod
    def RaiseValueError(var, floor=0) -> None:
        Error.RaiseTypeError(var, int)
        if var < floor:
            raise ValueError(
                f"Value does not fit in parameters. {var} is less than [floor]: {floor}"
            )


class Files:
    def __init__(self, path="Files/"):
        self.path_to_dir = path

    def set_dir(self, path):
        self.path_to_dir = path

    @property
    def path(self):
        return self.path_to_dir

    def rename(self):
        path = self.path_to_dir
        file_list = os.listdir(path)

        for i, filename in enumerate(file_list, 1):
            printy(f"[c]{i}.@ [y]{filename}@")

        # Ask the user for input on which files to rename
        selected_numbers = [
            int(num.strip())
            for num in inputy(
                "Enter the numbers of the files you want to rename [g](comma-separated)@: "
            ).split(",")
        ]

        # Iterate through the selected files and rename them
        for num in selected_numbers:
            if 1 <= num <= len(file_list):
                selected_file = file_list[num - 1]
                (
                    name,
                    extension,
                ) = os.path.splitext(selected_file)

                new_filename = f"{inputy('Enter a new name for {selected_file} (without extension): ')}{extension}"

                old_file_path = os.path.join(
                    path,
                    selected_file,
                )
                new_file_path = os.path.join(
                    path,
                    new_filename,
                )

                os.rename(
                    old_file_path,
                    new_file_path,
                )
                print(f"{selected_file} has been renamed to {new_filename}")
            else:
                print(f"Invalid selection: {num}")

        printy(
            "File names have been changed.",
            "y",
        )


class Visuals:
    def __init__(self):
        pass


class Loading(Visuals):
    def __init__(self):
        super().__init__()


class Text(Visuals):
    def __init__(self):
        super().__init__()

    @staticmethod
    def Banner(text, font="slant", color="y"):
        f = Figlet(font=font)
        printy(f.renderText(text), color)

    @staticmethod
    def Clear():
        os.system("cls")


class Banner(Text):
    def __init__(self):
        super().__init__()


class Verification:
    def __init__(self):
        pass


class URL(Verification):
    @staticmethod
    def verify():
        return True


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def Speak(self, text: list) -> object:
        if not isinstance(text, list):
            raise TypeError("Must be a list.")

        for t in text:
            printy(text, "g")
            self.engine.say(text)
        printy("\[complete\]", "y")
        self.engine.runAndWait()

    def Save(
        self,
        message: str,
        file_name: str,
    ):
        if not isinstance(message, str) and not isinstance(file_name, str):
            raise TypeError("Must be string (str).")

        self.engine.save_to_file(
            message,
            f"/Files/{file_name}.mp3",
        )
        self.engine.runAndWait()
