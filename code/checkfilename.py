import json
import os
import shutil
import glob

def extract_image_names(file_path):
    # Read JSON content from the text file
    with open(file_path, 'r') as file:
        json_content = json.load(file)

    # Extract image names from the JSON content
    image_names = [entry["name"] for entry in json_content]

    return image_names

def check_images_exist(image_names, base_dir):
    print("entered check_images_exist ")
    # Check if each image file exists in the specified directory and its subdirectories
    present_images = []
    missing_images = []
    
    # for foldername, _, filenames in os.walk(base_dir):
    #     for filename in filenames:
    #         if filename in image_names:
    #             present_images.append(os.path.join(foldername, filename))
    #             image_names.remove(filename)

    filenames = sorted( filter( os.path.isfile,
                          glob.glob(base_dir + '/**/*', recursive=True) ) )
    for filename in filenames:
        filename = os.path.basename(filename)
        if filename in image_names:
            present_images.append(filename)
            image_names.remove(filename)

    missing_images = image_names

    return present_images, missing_images
    
def copy_images(image_names, source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)
    # Copy each image to the destination directory
    for image_name in image_names:
        filename = os.path.basename(image_name)
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        if os.path.exists(source_path):
            print(source_path, destination_path)
            shutil.copy(source_path, destination_path)
            print(f"Image '{image_name}' copied to '{destination_dir}'")
        else:
            print(f"Image '{image_name}' not found in '{source_dir}'")

# Example usage
if __name__ == "__main__":
    json_file_path = 'C:\\Ravi\\AIML\\Capstone\\bdd100k\\labels\\bdd100k_labels_images_val.json'
    base_directory = r'C:\Ravi\AIML\Capstone\bdd100k\images\100k\val'
    destination_directory = r'C:\Ravi\AIML\Capstone\bdd100k\images\100k\val_mod'

    # Extract image names from the JSON file
    image_names = extract_image_names(json_file_path)

    # Check if images exist in the specified directory and its subdirectories
    present, missing = check_images_exist(image_names, base_directory)

    print("my Present images below", "count of present images:", len(present))
    for file in present:
        print(file, "\n")

    print("my missing images below", "count of missing images:", len(missing))
    for file in missing:
        print(file, "\n")

    copy_images(present, base_directory, destination_directory)
