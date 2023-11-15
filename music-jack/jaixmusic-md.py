import scipy.io.wavfile
from printy import inputy
from transformers import pipeline

from SysManager.systems_check import check_gpu

check_gpu()

prompt = None  # inputy("Enter the prompt: ", "Ic")

with open("music-jack/jaixmusic-sm.py", "r") as f:
    prompt = f.read()

config = {
    "file": prompt[10:],
}
# Initialize the text-to-audio pipeline
synthesiser = pipeline("text-to-audio", "facebook/musicgen-medium")

# Generate the music
music = synthesiser(f"{prompt}", forward_params={"do_sample": True})

# Write the generated music to a WAV file
scipy.io.wavfile.write(
    f"music/{config['file'][10:]}.wav".replace(" ", "_"),
    rate=music["sampling_rate"],
    data=music["audio"],
)
