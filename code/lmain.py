from bdd100k_prepare_dataset import *
from projutils import *
from defines import *

# Train
input_directory = "C:\\Ravi\\AIML\\Capstone\\bdd100k\\images\\100k\\train_mod"
output_directory = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images\\train"
image_size = (640, 640)

# Resize and save the images#
#resize_and_save_images(input_directory, output_directory, new_size=image_size)
#bdd100klabeltoYOLOlabelformat(label_json_path,labels_path,image_size,class_labels)

# Val
input_directory = "C:\\Ravi\\AIML\\Capstone\\bdd100k\\images\\100k\\val_mod"
output_directory = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images\\val"
image_size = (640, 640)

#resize_and_save_images(input_directory, output_directory, new_size=image_size)
#bdd100klabeltoYOLOlabelformat(label_json_path,labels_path,image_size,class_labels)

#Test
input_directory = "C:\\Ravi\\AIML\\Capstone\\bdd100k\\images\\100k\\test"
output_directory = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images\\test"
image_size = (640, 640)

resize_and_save_images(input_directory, output_directory, new_size=image_size)

label_json_path = "C:\\Ravi\\AIML\\Capstone\\bdd100k\\labels\\bdd100k_labels_images_val.json"
images_path = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images\\"
labels_path = "C:\\Ravi\\AIML\\Capstone\\temp_data\\labels\\val"
dest_path = "C:\\Ravi\\AIML\\Capstone\\"


#bdd100klabeltoYOLOlabelformat(label_json_path,labels_path,image_size,class_labels)





#bdd100klabeltoYOLOlabelformat(label_json_path,labels_path,image_size,class_labels)
label_json_path = "C:\\Ravi\\AIML\\Capstone\\bdd100k\\labels\\bdd100k_labels_images_val.json"
images_path = "C:\\Ravi\\AIML\\Capstone\\temp_data\\images\\"
labels_path = "C:\\Ravi\\AIML\\Capstone\\temp_data\\labels"
dest_path = "C:\\Ravi\\AIML\\Capstone\\"

preparesample(images_path,labels_path,dest_path,train_sample_size=100,val_sample_size=10,test_sample_size=10)