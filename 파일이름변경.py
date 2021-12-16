import os


# # 1.
# folders=['smile','wonder','angry']
# for folder in folders:
#     file_path = './data/face/'
#     file_path+=folder
#     # print(file_path)
#     file_names = os.listdir(file_path)
#     file_names

#     i = 1
#     for name in file_names:
#         src = os.path.join(file_path, name)
#         dst = folder+str(i) + '.jpg'
#         dst = os.path.join(file_path, dst)
#         os.rename(src, dst)
#         i += 1



# 2. sad폴더에서 'crying face'파일의 공백 -> 'crying_face'로 치환

file_path = './dataset/face/angry'
file_names = os.listdir(file_path)

i=1
for name in file_names:
    src = os.path.join(file_path, name)
    print(src)
    # dst = name.replace(' ','_',1)
    dst='angry'+str(i)+'.jpg'
    i+=1
    # print(dst)
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
