# JackTube 1.0A

import os
from copy import deepcopy

from printy import printy
from pytube import YouTube as JTube


class Audio:
    def __init__(self):
        self.input_file = "/home/sohfix0/Music/input.txt"
        self.url_list = []
        self.title_list = []
        self.zip_list = []
        self.type = type

    def Add(self, link: str) -> None:
        self.url_list.append(str(link))
        printy("[g]URL@ added to the [y]queue@.")

    def QuickAdd(self) -> None:
        try:
            with open(self.input_file, "r") as f:
                v_temp = f.readline()
            for e in v_temp:
                self.url_list.append(v_temp)

            printy(f"All files have been added to the [y]list@.\n")
        except EOFError:
            printy("An [r]error@ has occurred, yo!", "y")

    @property
    def Queue(self) -> list:
        return self.url_list

    @property
    def URL_List(self) -> list:
        return deepcopy(self.url_list)


class YouTubeAudio(Audio):
    def __init__(self, a_type=".mp3"):
        super().__init__()
        self.type = a_type

    def Download(self):
        for i in self.url_list:
            try:
                temp = self.url_list.pop(0)
                JackTube = JTube(str(temp))
                self.title_list.append(JackTube.title)

                # extract only audio
                video = JackTube.streams.filter(only_audio=True).first()  # audio
                print('downloading video: ', JackTube.title)
                out_file = video.download(
                    output_path="/home/sohfix0/Music/"
                )  # download

                # save the file
                base, _ = os.path.splitext(out_file)
                new_file = base + self.type + ""

                os.rename(out_file, new_file)
                printy(
                    f"[y]{JackTube.title}@ [g]has been successfully@ [y]downloaded@."
                )
            except FileExistsError as e:
                printy(
                    f"\n[o]{JackTube.title}@ already exists.  [g]Error#@: {e.errno}\n"
                )
                break
            finally:
                pass
