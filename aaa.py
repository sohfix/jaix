import scipy
from transformers import pipeline

from SysManager.systems import log_text as log

inp = ""

with open("bark.txt", "w") as f:
    inp = f.readline()

synthesiser = pipeline("text-to-speech", "suno/bark")
speech = synthesiser(inp, forward_params={"do_sample": True})

scipy.io.wavfile.write(
    "bark_out.wav", rate=speech["sampling_rate"], data=speech["audio"]
)
