import augmentor
import os
import numpy as np
import cv2
import matplotlib.image as mimg
import sys

def generate(n_images):
    try:
        os.mkdir("./temp_data") #making folder to save the images
    except:
        print("Folder already exsist")

    raw_data_path = "./hindi_data/"
    folder_list = list(os.walk(raw_data_path))[0][1]
    count = 0
    for j in range(2,8):#for no: characters in image
        for i in range(int(n_images)): # no: of images
            folder_no = np.random.randint(0,len(folder_list))
            img_list = list(os.walk(raw_data_path+folder_list[folder_no]))[0][2]
            img_no = np.random.randint(0,len(img_list))
            img = cv2.imread(raw_data_path+folder_list[folder_no]+"/"+img_list[img_no])
            name = folder_list[folder_no]+"_"
            for k in range(j-1): #for no: of characters in image
                folder_no = np.random.randint(0,len(folder_list))
                img_list = list(os.walk(raw_data_path+folder_list[folder_no]))[0][2]
                img_no = np.random.randint(0,len(img_list))
                img2 = cv2.imread(raw_data_path+folder_list[folder_no]+"/"+img_list[img_no])
                img = np.concatenate((img,img2),axis = 1)
                name = name+folder_list[folder_no]+"_"
            count = count+1
            if count%100==0:
                print(str(count)+" images done")
            img = cv2.line(img,(3,5),(img.shape[1]-2,5),(0,0,0),2) #drawing line over the letters 
            mimg.imsave("./temp_data/"+name+".png",img)
    augmentor.augment()
    os.system("rm -r temp_data")

if __name__ == "__main__":
    if len(sys.argv)>1:
        generate(int(sys.argv[1]))
    else:
        generate(100)
    