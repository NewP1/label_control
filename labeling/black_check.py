from glob import glob
import cv2
import os
import keyboard
import numpy as np


classes = {  0: '셔츠/블라우스', 1: '상의/티셔츠/맨투맨/스웨터', 2: '자켓/카디건',  3: '조끼',  4: '바지',  5: '반바지',  6: '치마',  7: '코트',  8: '드레스/원피스',
    9: '안경/선글라스',  10: '모자',  11: '머리띠', 12: '신발',  13: '가방/지갑',  14: '스카프', 15:'검은색 상의', 16:'검은색 외투'}

color = [[0,0,255], [0,255,0], [255,0,0],[255,255,0], [255,0,255], [0,255,255]]

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")
        
def point_make(point_list, h, w, des_class):
    final = []
    des = [des_class] # [15, 16]
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
        
path = r'C:\Users\user\yolov8\images\train_resize\train'    # 이미지 경로

label_path = r'C:\Users\user\labeling\runs\train_1\jacket\sweatshirt'  # label 경로 

txts = glob(os.path.join(label_path, '*.txt'))

num = 190
rate = .8 
des_class = 16
change_dict = {0 : 15, 1 : 15, 2 : 16, 7 : 16, 16 : 7, 16 : 2}
len_max = len(txts)

for i in range(num, len_max):
    print('\n현재번호 : ', i,'/',len(txts))
    tmp = txts[i]
    t_src = tmp[len(label_path)+1:]
    src = t_src[:-4]
    j_file = os.path.join(path, src+'.jpg')

    with open(tmp,'r') as f:           # 해당 파일 txt 읽어오기
        lines = f.readlines()   
    o_label_result = []
    for line in lines:
        o_label_result.append(int(line.split()[0]))
        
    if des_class in o_label_result:
        print(tmp)
        print(j_file)
        for i in range(len(o_label_result)):
            o_label_result[i] = classes.get(o_label_result[i])
        print(o_label_result)
    

        show_src = cv2.imread(j_file)
        tmp_src = cv2.resize(show_src,None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)
        change_src = cv2.resize(show_src,None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)

        h, w = change_src.shape[:2]
        points = point_make(lines, h, w, des_class)
        
        for j in range(len(points)):
            p = points[j]
            p_array = np.array(p,dtype=np.int32)
            img = cv2.polylines(change_src, [p_array], True, color[j], 2)
            
        cv2.namedWindow('origin')
        cv2.namedWindow("img")
        cv2.imshow('origin', tmp_src)
        cv2.imshow('img', change_src)
        cv2.moveWindow(winname='origin', x=2000, y=80)
        cv2.moveWindow(winname='img', x=500, y=80)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        if keyboard.is_pressed('f'):
            break
        elif keyboard.is_pressed('s'):
            with open(tmp, 'w') as f:
                for line in lines:
                    line_list = line.split()
                    index = int(line_list[0])
                    if index == des_class:
                        line_list[0] = str(change_dict[des_class])
                    f.write(' '.join(line_list)+'\n')
                    
        with open(tmp,'r') as f:           # 해당 파일 txt 읽어오기
            lines = f.readlines()   
        o_label_result = []
        for line in lines:
            o_label_result.append(classes[int(line.split()[0])])  
        print(o_label_result)
        

    



