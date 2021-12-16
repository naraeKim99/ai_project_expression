# openCV 활용
# 자른얼굴 저장하기

import cv2

# haarcascade 불러오기
# 얼굴과 눈을 찾기위한 미리 학습된 샘플 데이터
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

import os
# 이미지 불러오기
# '샘플이미지경로': 얼굴을 검출하고싶은 이미지 경로를 작성해주세요

folders=['angry2']  #,'wonder''smile','angry','sad','impassive'
for folder in folders:
    i=1
    # print(folder)
    for filename in os.listdir ('./data/face/'+folder):

        # print(filename)
        img = cv2.imread('./data/face/'+folder+'/'+filename)
        # 이미지 전처리
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 얼굴 찾기
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # print(img)
        # print(faces)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if x != 0 and y!=0 and w != 0 and h != 0:
                print(x, y, w, h)
                test_cut = img[y:y+h, x:x+w]

                cv2.imshow('image', test_cut)
                cv2.imwrite('./data/newimg/'+folder+'/'+filename,test_cut)


key = cv2.waitKey(0)
cv2.destroyAllWindows()