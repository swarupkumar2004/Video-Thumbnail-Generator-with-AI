from utils.frame_utils import extract_keyframes
from utils.yolo_utils import detect_objects
from utils.face_utils import detect_faces
from utils.scene_utils import classify_scene
from utils.color_utils import extract_palette

from PIL import Image, ImageDraw, ImageFont
import cv2, os

def generate_thumbnail(video_path, output_path):
    keyframes = extract_keyframes(video_path)
    if not keyframes:
        print(f"No keyframes found in: {video_path}")
        return

    best_frame = keyframes[0]

    yolo_results = detect_objects(best_frame)
    face_boxes = detect_faces(best_frame)
    scene = classify_scene(best_frame)
    colors = extract_palette(best_frame)

    img = Image.fromarray(cv2.cvtColor(best_frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    draw.text((20, 20), f"{scene['label']} 🔥", font=font, fill=(255, 0, 0))

    for label, conf, (x1, y1, x2, y2) in yolo_results:
        draw.rectangle([(x1, y1), (x2, y2)], outline="blue", width=3)
        draw.text((x1, y1 - 25), f"{label} ({conf:.2f})", fill="blue", font=font)

    for (x, y, w, h) in face_boxes:
        draw.rectangle([(x, y), (x + w, y + h)], outline="green", width=3)

    img.save(output_path)
    print(f"Thumbnail saved: {output_path}")

# run for one video
if __name__ == "__main__":
    input_path = "videos/sample.mp4"
    output_path = "thumbnails/sample_thumbnail.jpg"
    os.makedirs("thumbnails", exist_ok=True)
    generate_thumbnail(input_path, output_path)
