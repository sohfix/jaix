import scipy.io.wavfile as wav
from transformers import pipeline

from SysManager.systems import check_gpu, check_os, log_text

prompt = check_gpu()

with open("song_p.txt", "r") as f:
    for i in range(1, 2):
        while prompt:
            prompt = f.readline().strip()
            print(prompt)
            log_text(
                f"test run{i} - prompt:{prompt} >",
            )

            synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

            music = synthesiser(f"{prompt}", forward_params={"do_sample": True})

            wav.write(
                f"music/{str(prompt).replace(' ', '_')}.wav",
                rate=music["sampling_rate"],
                data=music["audio"],
            )
