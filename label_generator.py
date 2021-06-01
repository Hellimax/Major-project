import os
import cv2
import json
import numpy as np

def generate_labels():
    
    img_list = list(os.walk("./train_data"))[0][2]
    max_len_image = max(list(os.walk("./train_data/"))[0][2],key=len)
    max_char_len = len(max_len_image.split("_"))-1
    max_len_image = cv2.imread("./train_data/"+max_len_image).shape[1]

    blank = cv2.imread("./blank.png")
    train_len = int((len(img_list)*95)/100)
    with open("./data/index_to_char.json","r") as f:
        index_to_char = json.load(f)
    
    

    with open("train_labels.txt","w") as file:
        for i in range(0,train_len):
            img_name = img_list[i].split("_")
            img = cv2.imread("./train_data/"+img_list[i])
            while img.shape[1]!=max_len_image:
                img = np.concatenate((img,blank),axis=1)
            cv2.imwrite("./train_data/"+img_list[i],img)
            label = ""
            for j in range(len(img_name)-1):
                label = label+index_to_char[img_name[j]]
            if len(img_name)-1<max_char_len:
                label = label+(max_char_len-(len(img_name)-1))*"@"
            
            file.write("./train_data/"+img_list[i]+" "+label+"\n")

            if i%1000==0:
                print(str(i)+" train images done")

    with open("test_labels.txt","w") as file:
        for i in range(train_len,len(img_list)):
            img_name = img_list[i].split("_")
            img = cv2.imread("./train_data/"+img_list[i])
            while img.shape[1]!=max_len_image:
                img = np.concatenate((img,blank),axis=1)
            cv2.imwrite("./train_data/"+img_list[i],img)
            label = ""
            for j in range(len(img_name)-1):
                label = label+index_to_char[img_name[j]]
            if len(img_name)-1<max_char_len:
                label = label+(max_char_len-(len(img_name)-1))*"@"
            
            file.write("./train_data/"+img_list[i]+" "+label+"\n")
            if i%1000==0:
                print(str(i)+" test images done")


if __name__=="__main__":
    generate_labels()