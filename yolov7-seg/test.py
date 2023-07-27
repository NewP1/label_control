from glob import glob
import cv2
import os
import tqdm
import keyboard


# 0 ~ 2041
# 정검지 카운터

num = 2014
c_count = 1205
# 110 번까지 자켓 코트 재확인 필요 현재 65


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

d = {  0: '셔츠/블라우스',  1: '상의/티셔츠/맨투맨', 2: '자켓',  3: '조끼',  4: '바지',  5: '반바지',  6: '치마',  7: '코트',
     8: '드레스/원피스', 9: '안경/선글라스', 10: '모자',  11: '머리띠',  12: '신발',  13: '가방/지갑',  14: '스카프'}
        
path = r'C:\Users\user\yolov7-seg\test'
path_origin = os.path.join(path, 'test_ori')
path_result = os.path.join(path, 'result')
path_labels = os.path.join(path, 'labels')

ori_imgs = glob(os.path.join(path_origin, '*.jpg'))
res_imgs = glob(os.path.join(path_result, '*.jpg'))
labels = glob(os.path.join(path_labels, '*.txt'))

rate = 2

print("\n처음 정검지 카운트 : ", c_count)

i = num

while(i<2042 and i>=0):

    print('----------------------------------------')
    print("\n현재 번호 : ", i)
    label_result = []
    
    if keyboard.is_pressed('f'):
        break  
    elif keyboard.is_pressed('c'):
        c_count += 1
        print('\t\t\t\t + 1')

    print("현재 정검지 카운트 : ", c_count)
    print("\n현재 오검지 카운트 : ", i - c_count)

    with open(labels[i],'r') as f:
        text = f.readlines()
    for line in text:
        label_result.append(d[int(line.split()[0])])
    print()
    print(label_result)


    show_ori = cv2.imread(ori_imgs[i])
    show_res = cv2.imread(res_imgs[i])
    change_res = cv2.resize(show_res, None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)

    tmp = res_imgs[num][len(path_result)+1:]
    print('\n현재 퍼센트 : ',round(100*(c_count/i),2),'%')

    i += 1
    cv2.namedWindow('origin')
    cv2.namedWindow('seg')
    cv2.imshow('origin',show_ori)
    cv2.imshow('seg',change_res)
    cv2.moveWindow(winname='origin', x=250, y=250)
    cv2.moveWindow(winname='seg', x=1000, y=250)
    # cv2.resizeWindow(winname='origin', width=600, height=150)
    # cv2.resizeWindow(winname='seg', width=200, height=150)
    cv2.waitKey(0)    
    cv2.destroyAllWindows()



# c = int(input('정검지 : 1 , 오검지 : 0 == '))

# if c == 1:
#     des = os.path.join(path, 'success')
#     createDirectory(des)
#     cv2.imwrite(os.path.join(des, tmp), show_res)
#     l_des = os.path.join(des, 'labels')
#     createDirectory(l_des)
#     with open(os.path.join(l_des, labels[num][len(path_labels)+1:]),'w') as f:
#         for line in text:
#             f.write(line)
# elif c == 0:
#     des = os.path.join(path, 'fail')
#     createDirectory(des)
#     cv2.imwrite(os.path.join(des,tmp), show_res)
#     l_des = os.path.join(des, 'labels')
#     createDirectory(l_des)
#     with open(os.path.join(l_des, labels[num][len(path_labels)+1:]),'w') as f:
#         for line in text:
#             f.write(line)
