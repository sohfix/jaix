import time
from huggingface_hub import snapshot_download
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline
import torch

# Set default tensor type to CPU tensor
torch.set_default_tensor_type(torch.FloatTensor)

s = time.time()

# Read the prompt from 'input.txt'
with open("/home/sohfix0/Documents/models/jaix/ttv/input.txt", "r") as f:
    prompt = f.readline().strip()

# Download the model
model_dir = snapshot_download(
    "damo-vilab/modelscope-damo-text-to-video-synthesis", repo_type="model"
)

# Set up the pipeline - specify to use CPU
pipe = pipeline("text-to-video-synthesis", model_dir, device="cpu")

# Generate the video
test_text = {"text": prompt}
output_video_path = pipe(test_text)[OutputKeys.OUTPUT_VIDEO]

# Print the output video path
print("Output video path:", output_video_path)

e = time.time()
print("Time taken:", e - s)
