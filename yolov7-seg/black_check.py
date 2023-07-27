from glob import glob
import cv2
import os
import keyboard

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")
        
path = r'C:\Users\user\AIHub_seg\runs\segment\predict_afternoon_seg'
jpg = glob(os.path.join(path, '*.jpg'))

rate = 3

check_count = 4500
black_count = 0
not_count = 4500


for i in range(check_count, len(jpg)):
    print("\n본 개수 : ", i+1)
    jpg_file = jpg[i]
    print(jpg_file)
    if keyboard.is_pressed('f'):
        break
    elif keyboard.is_pressed('s'):
        black_count += 1
        print('\t\t\t\t + 1')
    else:
        not_count += 1
        
        
    print("검은 옷 개수 : ", black_count)
    print("일반 옷 개수 : ", not_count)
    print('\n-----------------------')
    show_src = cv2.imread(jpg_file)
    change_src = cv2.resize(show_src,None, fx=rate, fy=rate, interpolation=cv2.INTER_AREA)
    
    cv2.namedWindow("img")
    cv2.imshow('img', change_src)
    cv2.moveWindow(winname='img', x=850, y=80)
    cv2.waitKey(0)
    cv2.destroyAllWindows()