# cnn데이터증강_표정
# 이미지를 dataset으로 변형.
# 이미지가 카테고리별로 분류되어 있을 때

import os, shutil
from re import X
import pickle 
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# 이미지 전처리 유틸리티 모듈
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import matplotlib.pyplot as plt
from tensorflow.keras import optimizers

import numpy as np 
import os 
import random 
import PIL.Image as pilimg
import imghdr
import pandas as pd 
import tensorflow as tf
from PIL import Image

# https://www.tensorflow.org/tutorials/images/classification



# 원본 데이터셋을 압축 해제한 디렉터리 경로-원래 이미지 있는 폴더 
original_smile_dir = './dataset/face/smile'
original_angry_dir = './dataset/face/angry'
original_impassive_dir = './dataset/face/impassive'
original_sad_dir = './dataset/face/sad'
original_wonder_dir = './dataset/face/wonder'


#옮길 위치 
base_dir = './dataset/small_face'

train_dir = os.path.join(base_dir, 'train')
test_dir = os.path.join(base_dir, 'test')

#-------------------------------------
train_smile_dir = os.path.join(train_dir, 'smile')
train_impassive_dir = os.path.join(train_dir, 'impassive')
train_angry_dir = os.path.join(train_dir, 'angry')
train_sad_dir = os.path.join(train_dir, 'sad')
train_wonder_dir = os.path.join(train_dir, 'wonder')

test_smile_dir = os.path.join(test_dir, 'smile')
test_impassive_dir = os.path.join(test_dir, 'impassive')
test_angry_dir = os.path.join(test_dir, 'angry')
test_sad_dir = os.path.join(test_dir, 'sad')
test_wonder_dir = os.path.join(test_dir, 'wonder')



# dataset 나누기
# 방법 1. 이미지를 ndarray로 바꾸기 위해 복사먼저 한다.
# 방법 2. 그러나 ndarray로 바꾸지 않기 위해 ImageDataGenerator 사용 - 데이터 많을 때 더 유용
def ImageCopyMove():
    
    # 반복적인 실행을 위해 디렉토리를 삭제합니다.
    if os.path.exists(base_dir):  #기존에 디렉토리가 존재하면 전부 지우기 
        shutil.rmtree(base_dir, ignore_errors=True, onerror=None)   
    
    #새로폴더만들기
    os.mkdir(base_dir) #없으면 만들기 

    os.mkdir(train_dir)
    os.mkdir(test_dir)

    os.mkdir(train_smile_dir)
    os.mkdir(train_impassive_dir)
    os.mkdir(train_angry_dir)
    os.mkdir(train_sad_dir)
    os.mkdir(train_wonder_dir)

    os.mkdir(test_smile_dir)
    os.mkdir(test_impassive_dir)
    os.mkdir(test_angry_dir)
    os.mkdir(test_sad_dir)
    os.mkdir(test_wonder_dir)



    # 처음 500개의 smile 이미지를 train_smile_dir에 복사합니다
    fnames = ['smile{}.jpg'.format(i) for i in range(1,801)]
    for fname in fnames:
        src = os.path.join(original_smile_dir, fname)
        dst = os.path.join(train_smile_dir, fname)
        shutil.copyfile(src, dst)
    
    # 마지막 남은 smile 이미지를 test_smile_dir에 복사합니다
    fnames = ['smile{}.jpg'.format(i) for i in range(801, 1099)]
    for fname in fnames:
        src = os.path.join(original_smile_dir, fname)
        dst = os.path.join(test_smile_dir, fname)
        shutil.copyfile(src, dst)



    fnames = ['angry{}.jpg'.format(i) for i in range(1,801)]
    for fname in fnames:
        src = os.path.join(original_angry_dir, fname)
        dst = os.path.join(train_angry_dir, fname)
        shutil.copyfile(src, dst)
    
    fnames = ['angry{}.jpg'.format(i) for i in range(801, 1036)]
    for fname in fnames:
        src = os.path.join(original_angry_dir, fname)
        dst = os.path.join(test_angry_dir, fname)
        shutil.copyfile(src, dst)



    fnames = ['impassive{}.jpg'.format(i) for i in range(1,901)]
    for fname in fnames:
        src = os.path.join(original_impassive_dir, fname)
        dst = os.path.join(train_impassive_dir, fname)
        shutil.copyfile(src, dst)
    
    fnames = ['impassive{}.jpg'.format(i) for i in range(901, 1123)]
    for fname in fnames:
        src = os.path.join(original_impassive_dir, fname)
        dst = os.path.join(test_impassive_dir, fname)
        shutil.copyfile(src, dst)
    


    fnames = ['sad{}.jpg'.format(i) for i in range(1,661)]
    for fname in fnames:
        src = os.path.join(original_sad_dir, fname)
        dst = os.path.join(train_sad_dir, fname)
        shutil.copyfile(src, dst)
    
    fnames = ['sad{}.jpg'.format(i) for i in range(661, 893)]
    for fname in fnames:
        src = os.path.join(original_sad_dir, fname)
        dst = os.path.join(test_sad_dir, fname)
        shutil.copyfile(src, dst)



    fnames = ['wonder{}.jpg'.format(i) for i in range(1,801)]
    for fname in fnames:
        src = os.path.join(original_wonder_dir, fname)
        dst = os.path.join(train_wonder_dir, fname)
        shutil.copyfile(src, dst)
    
    fnames = ['wonder{}.jpg'.format(i) for i in range(801, 1012)]
    for fname in fnames:
        src = os.path.join(original_wonder_dir, fname)
        dst = os.path.join(test_wonder_dir, fname)
        shutil.copyfile(src, dst)
# ImageCopyMove()




# 데이터증강_dogcat3의 DataIncrease함수
def study():
        batch_size = 32  #한번에 불러오는 이미지 개수 
        img_height = 180 #이미지의 높이 
        img_width = 180  #이미지의 넓이 

        data_augmentation = keras.Sequential(
                [
                        layers.experimental.preprocessing.RandomFlip("horizontal", 
                                                                input_shape=(img_height, img_width, 3)),
                        layers.experimental.preprocessing.RandomRotation(0.1),
                        layers.experimental.preprocessing.RandomZoom(0.1),
                ]
        )

        model = models.Sequential()

        model.add(data_augmentation)
        model.add(layers.experimental.preprocessing.Rescaling(1./255))  # 스케일링

        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(256, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(512, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten()) 
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(5, activation='softmax'))

        model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

        train_dir='./dataset/small_face/train'
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="training",    
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)

        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="validation",  
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)

        epochs=20
        history = model.fit(
                # train_ds,   # 데이터 증강 안할 떄
                train_ds.repeat(30),  # 데이터 증강 할 때
                validation_data=val_ds,
                epochs=epochs
        )
        

        # 모델 저장하기 
        model.save('face.h5')
        f=open('face_hist.hist','wb')
        pickle.dump(history.history, file=f)
        f.close()     



def drawChart():
    # 저장된 예측모델 load
    f=open('face_hist.hist','rb')
    history=pickle.load(f)
    f.close()

    acc = history['accuracy']
    val_acc = history['val_accuracy']
    loss = history['loss']
    val_loss = history['val_loss']

    epochs = range(len(acc))

    plt.plot(epochs, acc, 'bo', label='Training acc')
    plt.plot(epochs, val_acc, 'b', label='Validation acc')
    plt.title('Training accuracy')
    plt.legend()

    plt.figure()

    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training loss')
    plt.legend()

    plt.show()


# 사진 한개 예측하기 전에 모델의 예측력을 판단하기 위한 함수로 사용된다.
def exPredict():
        # 저장된 예측모델 load
        model = load_model("face.h5")
        test_dir = "./dataset/small_face/test"
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
                test_dir,
                seed=123,
                image_size=(180, 180),
                batch_size=1)
        # class_names = test_ds.class_names
        # print(class_names)

        print("---- Predict ----")
        print(test_ds)
        print('데이터 개수 :', tf.data.experimental.cardinality(test_ds).numpy())
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        
        # 데이터셋은 한번에 예측이 안된다 -> for문으로 하나씩 돌려야한다. -> batch_size=1
        # 일반적으로 test set이 두개 이상일 때.
        # 한개일 때는 밑에 함수 Predict에 예시 있다.
        match_cnt=0
        i=0
        emotions=test_ds.class_names
        
        for images, labels in test_ds:
                # images에 우리가 넣고싶은 이미지의 ndarray 넣으면
                output=model.predict(images)
                images=np.array(images)
                # print(images.shape)
                # print('라벨 :' ,labels)
                # print(' np.argmax(output) : ',  np.argmax(output))
                if labels==np.argmax(output):
                        match_cnt+=1
                        # print('감정 :', emotions[np.argmax(output)])
                        print(emotions[np.argmax(output)])
                else:
                        print('예측이 잘못되었습니다.')


        print("일치한 숫자 : ", match_cnt)
        print("불일치한 숫자 : ", tf.data.experimental.cardinality(test_ds).numpy()-match_cnt)



# 사진 한장만 예측하는 함수
def Predict():
        model = load_model("face.h5")
        test_dir = "./dataset/small_face/test"
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
                test_dir,
                seed=123,
                image_size=(180, 180),
                batch_size=1)

        print("---- Predict ----")
        print(test_ds)
        print('데이터 개수 :', tf.data.experimental.cardinality(test_ds).numpy())
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        
        # 데이터셋은 한번에 예측이 안된다 -> for문으로 하나씩 돌려야한다. -> batch_size=1
        match_cnt=0
        i=0
        emotions=test_ds.class_names
        

        # images에 우리가 넣고싶은 이미지의 ndarray 넣으면
        # 이미지 읽기 -> resize -> ndarray로 변환해야 한다 -> 위에 예측하기에서 shape출력해 그거에 맞게 reshape한다.
        images=Image.open('./angry813.jpg')
        images=images.resize((180,180))
        image=np.array(images)
        image=image.reshape(1,180,180,3)

        output=model.predict(image)
        # print('예측결과 :',emotions[np.argmax(output)])
        x=emotions[np.argmax(output)]
        x=x[0].upper()+x[1:]
        return x



def Evaluate():
        model=load_model('face.h5')
        batch_size = 32  #한번에 불러오는 이미지 개수 
        img_height = 180 #이미지의 높이 
        img_width = 180  #이미지의 넓이 

        train_dir='./dataset/small_face/train'
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="training",    # 훈련용
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)

        # 폴더에 validation set을 만들어 놓지 않고, train set을 train과 val set으로 나누며 사용된다.
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="validation",
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)

        test_dir = "./dataset/small_face/test"
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
                test_dir,
                seed=123,
                image_size=(180, 180),
                batch_size=32)

        print('훈련셋 :', model.evaluate(train_ds))
        print('검증셋 :', model.evaluate(val_ds))
        print('테스트셋 :', model.evaluate(test_ds))



if __name__=="__main__":
        while(True):
                print("1. 기본학습")
                print("2. 차트")
                print("3. 모델 예측하기")
                print("4. 최종 예측하기")
                print("5. 모델 평가하기")

                sel = input("선택 : ")
                if sel=="1":
                        study()
                elif sel=="2":
                        drawChart()
                elif sel=="3":
                        exPredict()
                elif sel=="4":
                        Predict()
                elif sel=="5":
                        Evaluate()        
                else:
                        break