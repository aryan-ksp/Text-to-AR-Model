import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image

def generate_depth_map(input_text):
    # Simulate a depth map (Grayscale noise for now)
    width, height = 256, 256
    depth_map = np.random.randint(50, 200, (height, width), dtype=np.uint8)

    # Save the depth map
    depth_map_path = "static/depth_map.png"
    cv2.imwrite(depth_map_path, depth_map)
    print(f"✅ Depth Map Saved: {depth_map_path}")

# Example usage
generate_depth_map("A futuristic car")
