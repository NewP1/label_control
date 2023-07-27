from glob import glob
import cv2
import os
import keyboard

d = {  0: '셔츠/블라우스',  1: '상의/티셔츠/맨투맨',  2: '스웨터',  3: '카디건',  4: '자켓',  5: '조끼',  6: '바지',  7: '반바지',  8: '치마',  9: '코트',  10: '드레스/원피스',
  11: '점프수트',  12: '망토',  13: '안경/선글라스',  14: '모자',  15: '머리띠',  16: '넥타이',  17: '장갑',  18: '시계',  19: '벨트/허리띠',  20: '다리보온대/레그워머',
  21: '타이즈/스타킹',  22: '양말',  23: '신발',  24: '가방/지갑',  25: '스카프',  26: '우산',  27: '후드/복면',  28: '카라/깃',  29: 'laped',  30: '어깨장식(견장)',
  31: '소매',  32: '주머니/호주머니',  33: '목둘레선',  34: '버클',  35: '지퍼',  36: '아플리케',  37: '구슬/염주',  38: '보타이',  39: '꽃',  40: '술',
  41: '리본',  42: 'rivet',  43: '주름장식',  44: '스팽글',  45: '술'}

des_classes = [0,1,4,5,6,7,8,9,10,13,14,15,23,24,25]


def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")

ori_path = r'C:\Users\user\yolov8\val_resize\resize_0.5'
ori_jpg = glob(os.path.join(ori_path, '*.jpg'))
ori_labels = r'C:\Users\user\yolov8\datasets\labels\val'
ori_txt = glob(os.path.join(ori_labels, '*.txt'))
        
fail_path = r'C:\Users\user\yolov8\runs\detect\resize_0.25\fail'
fail_labels = os.path.join(fail_path, 'labels')
fail_jpg = glob(os.path.join(fail_path, '*.jpg'))
fail_txt = glob(os.path.join(fail_labels, '*.txt'))

rate = 2

for i in range(len(fail_jpg)):
    print("\n본 개수 : ", i+1)
    jpg_file = fail_jpg[i]
    if keyboard.is_pressed('f'):
        break 
    tmp = jpg_file[len(fail_path)+1:]
    t_txt = tmp[:-4] + '.txt'

    f_label_result = []
    o_label_result = []


    if os.path.join(fail_labels, t_txt) in fail_txt:
        with open(os.path.join(fail_labels, t_txt),'r') as f:
            fail_text = f.readlines()
        for line in fail_text:
            if(int(line.split()[0]) in des_classes):
                f_label_result.append(d[int(line.split()[0])])

    with open(os.path.join(ori_labels, t_txt),'r') as f:
        ori_text = f.readlines()
    for line in ori_text:
            o_label_result.append(d[int(line.split()[0])])      
    print(jpg_file)  

    print('정상 label : ', sorted(o_label_result))
    print('fail label : ', sorted(f_label_result))

    show_ori = cv2.imread(os.path.join(ori_path, tmp))
    show_res = cv2.imread(os.path.join(fail_path, tmp))
    change_res = cv2.resize(show_res, None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)


    cv2.namedWindow('origin')
    cv2.namedWindow('fail')
    cv2.imshow('origin',show_ori)
    cv2.imshow('fail',change_res)
    cv2.moveWindow(winname='origin', x=250, y=250)
    cv2.moveWindow(winname='fail', x=1000, y=250)
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
