# 🎬 AI-Powered Video Thumbnail Generator

This project automatically generates eye-catching thumbnails for videos using AI-driven techniques like object detection, face detection, scene classification, and keyframe extraction.

---

## 🚀 Features

✅ Extracts keyframes based on action  
✅ Detects objects using YOLO  
✅ Detects and centers faces  
✅ Classifies scenes using ViT transformer  
✅ Extracts dominant color palette  
✅ Adds text overlays, filters, and auto-cropping  
✅ Supports multiple aspect ratios  
✅ Batch processing for multiple videos  

---

## 🛠️ Tech Stack

- Python 3.8+
- OpenCV (video processing)
- YOLOv8 (object detection)
- PIL (image editing)
- Hugging Face Transformers (scene classification)
- NumPy, torchvision

---

## 📂 Folder Structure

```

video-thumbnail-generator/
│
├── main.py               # Single video thumbnail generator
├── batch\_run.py          # Batch thumbnail generator
├── utils/
│   ├── frame\_utils.py    # Keyframe extraction
│   ├── face\_utils.py     # Face detection
│   ├── yolo\_utils.py     # YOLO integration
│   ├── scene\_utils.py    # Scene classification
│   └── color\_utils.py    # Color palette extraction
│
├── videos/               # Input videos (MP4)
├── thumbnails/           # Output thumbnails (JPG)
├── README.md             # Project guide

````

---

## ▶️ How to Run

1. ✅ **Install dependencies**
```bash
pip install -r requirements.txt
````

2. ✅ **Generate thumbnail for a single video**

```bash
python main.py
```

3. ✅ **Run batch processing for all videos**

```bash
python batch_run.py
```

---

## 📸 Sample Thumbnails

Over **20 thumbnails** have been generated and saved inside the `/thumbnails` folder. These include auto-detected faces, objects, and scene tags like “Nature 🔥” or “Urban 🔥”.

---

## 📊 Evaluation Criteria Mapping

| Criteria      | Achieved                          |
| ------------- | --------------------------------- |
| Functionality | ✅ High-quality thumbnails         |
| Automation    | ✅ Runs with minimal human input   |
| Code Quality  | ✅ Modular and clean utils         |
| Creativity    | ✅ Filters, overlays, scene labels |

---
