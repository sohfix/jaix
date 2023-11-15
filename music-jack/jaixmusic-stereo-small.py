import time
import scipy.io.wavfile
from transformers import pipeline

# Assuming check_gpu and log_text are correctly defined in SysManager.systems_check
from SysManager.systems_check import check_gpu, log_text

start = time.time()
modelj = "stereo-small"

check_gpu()

# Initialize the synthesizer outside of the loop
synthesiser = pipeline("text-to-audio", f"facebook/musicgen-{modelj}")

# Open and process each line in the file
with open("song_p.txt", "r") as f:
    for i, prompt in enumerate(f, start=1):
        prompt = prompt.strip()
        if prompt:  # Check if the line is not empty
            print(prompt)
            log_text(f"test run {i} | model: {modelj} - prompt: {prompt} >")

            music = synthesiser(prompt, forward_params={"do_sample": True})

            output_file = f"music-m/files-m-{i}.wav".replace(" ", "_")
            scipy.io.wavfile.write(
                output_file,
                rate=music["sampling_rate"],
                data=music["audio"],
            )
            log_text(f"Audio saved to {output_file}")

end = time.time()
print(f"Elapsed time: {end - start}")
log_text(f"Elapsed time: {end - start}")
