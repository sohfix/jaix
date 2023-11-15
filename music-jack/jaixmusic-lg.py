import time

import scipy.io.wavfile
from transformers import pipeline

# todo: add a check for GPU
from SysManager.systems_check import check_gpu, log_text

start, modelj, prompt = time.time(), "large", None

check_gpu()


with open("song_p.txt", "r") as f:
    for i in range(1, 2):
        while prompt:
            prompt = f.readline()
            print(prompt)
            log_text(
                f"test run{i} | model: {modelj} - prompt:{prompt} >",
            )

            synthesiser = pipeline("text-to-audio", f"facebook/musicgen-{modelj}")

            music = synthesiser(f"{prompt}", forward_params={"do_sample": True})

            scipy.io.wavfile.write(
                f"music-m/files-m-{i}.wav".replace(" ", "_"),
                rate=music["sampling_rate"],
                data=music["audio"],
            )

end = time.time()
print(f"Elapsed time: {end - start}")
log_text(f"Elapsed time: {end - start}")
