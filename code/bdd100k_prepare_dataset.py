import json
import os
from tqdm import tqdm
import shutil

def createfolderstructure(dirpath,empty_folder=False):
    #print(dirpath,os.path.exists(dirpath))
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)
    elif empty_folder:
        for f in os.listdir(dirpath):
            f_path = os.path.join(dirpath, f)
            if os.path.isfile(f_path):
                os.remove(f_path)
def bdd100klabeltoYOLOlabelformat(label_json_path,save_path,image_size,class_labels):
    with open(label_json_path) as json_file:
        data = json.load(json_file)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        for item in tqdm(data):
            file_name,content = converbddtoYOLOlabelformat(item,image_size,class_labels)
            writelabelfile(save_path+"//"+file_name,content)

def converbddtoYOLOlabelformat(item,image_size,class_labels):
    img_w, img_h = image_size
    img_name = str(item['name'][:-4])
    img_label_txt = img_name + ".txt"
    img_labels = [l for l in item['labels']]
    label_annotation =''
    for label in img_labels:
        y1 = label['box2d']['y1']
        x2 = label['box2d']['x2']
        x1 = label['box2d']['x1']
        y2 = label['box2d']['y2']
        class_name = label['category']
        class_id = class_labels[class_name]

        bbox_x = (x1 + x2) / 2
        bbox_y = (y1 + y2) / 2

        bbox_width = x2 - x1
        bbox_height = y2 - y1

        bbox_x_norm = bbox_x / img_w
        bbox_y_norm = bbox_y / img_h

        bbox_width_norm = bbox_width / img_w
        bbox_height_norm = bbox_height / img_h

        label_annotation += '{} {} {} {} {}\n'.format(
            class_id, bbox_x_norm, bbox_y_norm, bbox_width_norm, bbox_height_norm)
    return img_label_txt,label_annotation

def writelabelfile(file_path,content):
    with open(file_path, 'w+') as f_label:
        f_label.write(content + "\n")


def preparesample(img_source_path,label_source_path,dest_path,train_sample_size=100,val_sample_size=10,test_sample_size=10):
    print("training samples...")
    if train_sample_size > 0 and os.path.exists(label_source_path+"/train"):
        createfolderstructure(dest_path + "/labels/train",True)
        createfolderstructure(dest_path + "/images/train",True)
        cnt = 0
        for file in os.listdir(label_source_path+"/train"):
            cnt += 1
            img_file_name = file[:-4]+".jpg"
            shutil.copyfile(label_source_path+"/train"+"/"+file,dest_path+"/labels/train"+"/"+file)
            shutil.copyfile(img_source_path+"/train"+"/"+img_file_name,dest_path+"/images/train"+"/"+img_file_name)
            if cnt == train_sample_size:
                break

    print("validation samples...........")
    if val_sample_size > 0 and os.path.exists(label_source_path+"/val"):
        createfolderstructure(dest_path + "/labels/val",True)
        createfolderstructure(dest_path + "/images/val",True)
        cnt = 0
        for file in os.listdir(label_source_path+"/val"):
            cnt += 1
            img_file_name = file[:-4]+".jpg"
            shutil.copyfile(label_source_path+"/val"+"/"+file,dest_path+"/labels/val"+"/"+file)
            shutil.copyfile(img_source_path+"/val"+"/"+img_file_name,dest_path+"/images/val"+"/"+img_file_name)
            if cnt == val_sample_size:
                break

    print("test samples...")
    if test_sample_size > 0 and os.path.exists(label_source_path+"/test"):
        createfolderstructure(dest_path + "/labels/test",True)
        createfolderstructure(dest_path + "/images/test",True)
        cnt = 1
        for file in os.listdir(label_source_path+"/test"):
            cnt += 1
            img_file_name = file[:-4]+".jpg"
            shutil.copyfile(label_source_path+"/test"+"/"+file,dest_path+"/labels/test"+"/"+file)
            shutil.copyfile(img_source_path+"/test"+"/"+img_file_name,dest_path+"/images/test"+"/"+img_file_name)
            if cnt == test_sample_size:
                break

def frameextractor():
    pass