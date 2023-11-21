import random


def file_route(user='sohfix'):
    random_number = random.randint(1, 32)
    print(random_number)
    return f"/home/{user}/Music/{random_number}"
