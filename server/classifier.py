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


model = models.load_model('./model/face.h5')

def Predict(image):
        model = load_model("./model/face.h5")
        test_dir = "../dataset/small_face/test"
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
        images=Image.open(image)   # 이미지 경로
        images=images.resize((180,180))
        image=np.array(images)
        image=image.reshape(1,180,180,3)

        output=model.predict(image)
        # print('예측결과 :',emotions[np.argmax(output)])
        x=emotions[np.argmax(output)]
        if x=='smile':
                s='신나는 노래로 기분을 더 UP 시켜보세요 :)'
        elif x=='sad':
                s='이 음악들이 당신을 위로해줄 거예요 :)'
        elif x=='angry':
                s='이 음악들이 당신을 미소 짓게 해 주길 바라요 :)'
        elif x=='wonder':
                s='이 음악들로 마음을 가라앉혀 보세요 :)'
        else:
                s='이 음악들로 당신의 감정을 채워보세요 •᎑•'
        return x,s


if __name__ == '__main__': 
    x, sentence = Predict('./angry.jpg')
    print(sentence)
    