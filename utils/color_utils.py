import colorgram
import cv2
from PIL import Image
import numpy as np

def extract_palette(frame):
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    img.save("temp.jpg")
    colors = colorgram.extract("temp.jpg", 5)
    return [c.rgb for c in colors]
