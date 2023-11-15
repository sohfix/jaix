from transformers import pipeline
import scipy.io.wavfile
from printy import printy, inputy

config = {
    "path": inputy('Enter the path to the config file: ', 'y'),
    "prompt": inputy('Enter the prompt: ', 'y'),
}
# Initialize the text-to-audio pipeline
synthesiser = pipeline("text-to-audio", "facebook/musicgen-large")

# Generate the music
music = synthesiser(f"{config['prompt']}", forward_params={"do_sample": True})

# Write the generated music to a WAV file
scipy.io.wavfile.write(f"{config['prompt'][10:]}.wav", rate=music["sampling_rate"], data=music["audio"])
