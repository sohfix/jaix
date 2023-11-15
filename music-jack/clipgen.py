import scipy.io.wavfile
from transformers import AutoProcessor, MusicgenForConditionalGeneration

processor = AutoProcessor.from_pretrained("facebook/musicgen-small")
model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
output_audio = "musicgen_out1"
input_prompt = "bassy trap electronic bassnectar"

inputs = processor(
    text=[
        "lofi girl bass trap hardstyle",
    ],
    padding=True,
    return_tensors="pt",
)

audio_values = model.generate(
    **inputs, do_sample=True, guidance_scale=3, max_new_tokens=256
)
audio_numpy = audio_values.cpu().numpy()  # Convert tensor to numpy array

# Save the audio to a file
sampling_rate = 44100  # You might need to change this based on the model's output
scipy.io.wavfile.write(f"{output_audio}.wav", sampling_rate, audio_numpy)
