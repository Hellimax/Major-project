import os
import cv2
import tensorflow.keras.preprocessing.image as k_img 

def augment():
    try:
        os.mkdir("train_data")
    except:
        print("Folder already exsist")
    
    img_list = list(os.walk("./temp_data"))[0][2]

    augmentor = k_img.ImageDataGenerator(
        rotation_range=2,
        height_shift_range=0.3,
        brightness_range=[0.5,1.5],
        zoom_range=0.05
    )
    count = 0
    for i in img_list:
        img = cv2.imread("./temp_data/"+i)
        result = augmentor.flow(img.reshape((1,img.shape[0],img.shape[1],img.shape[2])),batch_size=1)
        for j in range(1):
            image = next(result)[0].astype('uint8')
            cv2.imwrite("./train_data/"+i,image)
        count = count+1
        if count%100==0:
            print(str(count)+" images augmented")


if __name__=="__main__":
    augment()