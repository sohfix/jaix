import torch


# print(torch.cuda.is_available())  # Should return True if the GPU is available
def alpha():
    return (
        "Fucking shit's at half capacity, boss."
        if torch.cuda.is_available()
        else "Wow, it works. Engines at full brew, Caption."
    )
