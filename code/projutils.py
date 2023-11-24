from PIL import Image
import cv2
import numpy as np
import os

def get_image_size(image_path):
    with Image.open(image_path) as img:
        return img.size
    
def resize_and_save_images(input_directory, output_directory, new_size):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)
        
        # Check if the file is an image (you might want to refine this check)
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            with Image.open(input_path) as img:
                # Resize the image
                resized_img = img.resize(new_size)
                
                # Save the resized image to the output directory
                output_path = os.path.join(output_directory, filename)
                resized_img.save(output_path)


if __name__ == "__main__":
    # Example usage
    input_directory = "C:\\Ravi\\AIML\\Capstone\\temp_data\\org_images"
    output_directory = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images"
    target_size = (640, 640)

    # Resize and save the images
    resize_and_save_images(input_directory, output_directory, new_size=target_size)
