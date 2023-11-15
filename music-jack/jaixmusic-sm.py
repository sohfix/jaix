import scipy.io.wavfile
from transformers import pipeline

from SysManager.systems_check import check_gpu, log_text

check_gpu()
prompt = 'robot metal hardstyle bass ethereal'

with open("song_p.txt", "r") as f:
    for i in range(5):
        while prompt:
            prompt = f.readline()
            print(prompt)
            log_text(f'test run{i} - prompt:{prompt} >',)

            config = {
                "file": prompt[10:],
            }

            synthesiser = pipeline("text-to-audio", "facebook/musicgen-small")

            music = synthesiser(f"{prompt}", forward_params={"do_sample": True})

            scipy.io.wavfile.write(
                f"music/{config['file'][10:]}.wav".replace(" ", "_"),
                rate=music["sampling_rate"],
                data=music["audio"],
            )
