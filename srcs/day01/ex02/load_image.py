from PIL import Image
import numpy as np
import os

def ft_load(path: str) -> any:
    print(path)
    if not os.path.exists(path):
        print("wrong path")
        return None
    try:
        img = Image.open(path)
        print("Image Format:", img.format)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img_array = np.array(img)
        print("Pixel Content (RGB Format):")
        for row in img_array:
            for pixel in row:
                print(tuple(pixel), end=' ')
            print()
        return img_array
        
    except Exception as e:
        print("Error loading image:", e)

ft_load("/usr/src/app/piscine/array/img/animal.jpeg")
