from glob import glob
import cv2
import os
import numpy as np
import keyboard

classes = {  0: '셔츠/블라우스',  1: '상의/티셔츠/맨투맨/스웨터', 2: '자켓/카디건',  3: '조끼',  4: '바지',  5: '반바지',  6: '치마',  7: '코트',  8: '드레스/원피스',
    9: '안경/선글라스',  10: '모자',  11: '머리띠', 12: '신발',  13: '가방/지갑',  14: '스카프', 15:'검은색 상의', 16:'검은색 외투'}


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")
        
def point_make(point_list, h, w):
    final = []
    des = [1]
    for line in point_list:
        result = []
        tmp = line.split()
        if int(tmp[0]) in des:
            tmp_points = tmp[1:]
            change_points = []
            for i in range(len(tmp_points)):
                if i % 2 == 0:
                    change_points.append(float(tmp_points[i]) * w)
                else:
                    change_points.append(float(tmp_points[i]) * h)
                    result.append(change_points)
                    change_points = []
            final.append(result)
    return final
    
        
num = 0
rate = .8
# des_class = 

j_file = r'C:\Users\user\yolov8\images\train_resize\train\338a10c808b2bf3ed2818131f214193b.jpg'
img = cv2.imread(j_file)
# print(img)
img = cv2.resize(img,None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)
h, w = img.shape[:2]

with open(r'C:\Users\user\labeling\runs\train\jacket\sweatshirt\338a10c808b2bf3ed2818131f214193b.txt','r') as f:           # 해당 파일 txt 읽어오기
    lines = f.readlines()
    
points = point_make(lines, h, w)


for p in points:
    p_array = np.array(p,dtype=np.int32)
    img = cv2.polylines(img, [p_array], True, (0,0,255), 2)
    
    cv2.namedWindow("seg")
    cv2.imshow('seg', img)
    cv2.moveWindow(winname='seg', x=2000, y=80)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
# path = r'C:\Users\user\Desktop\black_class\val\two_labels'

# jpg_path = os.path.join(path, 'two_jpg')

# for i in range(num, len(txts)):

#     print('\n현재번호 : ', i)
#     tmp = txts[i]
#     print(tmp)
#     t_src = tmp[len(path)+1:]
#     src = t_src[:-4]
#     j_file = os.path.join(jpg_path, src+'.jpg')
#     img = cv2.imread(j_file)
#     img = cv2.resize(img,None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)
#     h, w = img.shape[:2]

#     with open(tmp,'r') as f:           # 해당 파일 txt 읽어오기
#         lines = f.readlines()  
#     points = point_make(lines, h, w)
    

#     for p in points:
#         p_array = np.array(p,dtype=np.int32)
#         img = cv2.polylines(img, [p_array], True, (0,0,255))
        
#         cv2.namedWindow("img")
#         cv2.imshow('img', img)
#         cv2.moveWindow(winname='img', x=850, y=80)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     if keyboard.is_pressed('f'):
#         break