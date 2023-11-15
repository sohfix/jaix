import time

from huggingface_hub import snapshot_download
from modelscope.outputs import OutputKeys
from modelscope.pipelines import pipeline

from SysManager.systems_check import log_text

s = time.time()
# Read the prompt from 'input.txt'
with open("input.txt", "r") as f:
    prompt = f.readline().strip()

# Download the model
model_dir = snapshot_download(
    "damo-vilab/modelscope-damo-text-to-video-synthesis", repo_type="model"
)

# Set up the pipeline
pipe = pipeline("text-to-video-synthesis", model_dir)

# Generate the video
test_text = {"text": prompt}
output_video_path = pipe(test_text)[OutputKeys.OUTPUT_VIDEO]
log_text(f"Output video path: {output_video_path}")
log_text(test_text)
# Print the output video path
print("Output video path:", output_video_path)
e = time.time()
print("Time taken:", e - s)
log_text(f"Time taken: {e-s}")
