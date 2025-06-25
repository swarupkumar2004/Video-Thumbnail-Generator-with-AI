from transformers import pipeline
import cv2

classifier = pipeline("image-classification", model="google/vit-base-patch16-224") 


def classify_scene(frame):
    from PIL import Image
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    return classifier(img)[0] 
