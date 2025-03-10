from PIL import Image
import numpy as np

def display_image_info(image):
    print("Image Information:")
    print("Size (Width x Height):", image.size)
    print("Number of Channels:", len(image.getbands()))
    print("Pixel Content:")
    print(np.array(image))

def display_image_with_scale(image, scale=2):
    """
    i have to add the __doc__
    """
    width, height = image.size
    scaled_image = image.resize((width*scale, height*scale))
    scaled_width, scaled_height = scaled_image.size
    
    scale_marks = Image.new("RGB", (scaled_width, scaled_height), color="white")
    draw = Image.Draw.Draw(scale_marks)
    draw.line([(0, scaled_height - 20), (50, scaled_height - 20)], fill="black", width=2)
    draw.line([(scaled_width - 20, 0), (scaled_width - 20, 50)], fill="black", width=2)
    
    scaled_image.paste(scale_marks, (0, 0))
    
    scaled_image.show()

def main():
    
    try:
        image_path = "../img/animal.jpeg"
        image = Image.open(image_path)
        print(display_image_info.__doc__)
        display_image_info(image)
        display_image_with_scale(image)
        
    except FileNotFoundError:
        print("Error: Image file not found.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()