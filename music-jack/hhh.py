prompt = "o"

with open("song_p.txt", "r") as f:
    while prompt:
        prompt = f.readline()
        print(prompt)
