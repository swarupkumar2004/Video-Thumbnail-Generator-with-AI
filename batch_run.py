import os
from main import generate_thumbnail

video_dir = "videos"
output_dir = "thumbnails"
os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(video_dir):
    if file.endswith(".mp4"):
        input_path = os.path.join(video_dir, file)
        output_path = os.path.join(output_dir, file.replace(".mp4", "_thumb.jpg"))
        print(f"Processing {file}...")
        generate_thumbnail(input_path, output_path)
