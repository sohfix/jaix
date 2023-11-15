import torch


# print(torch.cuda.is_available())  # Should return True if the GPU is available
def check_gpu():
    return (
        "Fucking shit's at half capacity, boss."
        if torch.cuda.is_available()
        else "Wow, it works. Engines at full brew, Caption."
    )


def check_ram():
    pass


def check_cpu():
    pass


import datetime


def log_text(text, filename="logs/testing_log.txt"):
    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the file in append mode
    with open(filename, "a") as file:
        # Write the log entry
        file.write(f"[{current_time}]: {text}\n")