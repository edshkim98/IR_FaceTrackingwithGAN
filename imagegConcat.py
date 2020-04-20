import cv2
import os
import sys
import shutil


def img_stitch(image1,image2,a):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    img1 = cv2.resize(img1,(480,640))
    img2 = cv2.resize(img2,(480,640))
    addh = cv2.hconcat([img2,img1])
    cv2.imwrite(r'C:\shkim\Year3\Group research project\dataset\test\concat\\'+a,addh)

def jpgOnly(files):
    jpg = []
    for i in range(len(files)):
        if files[i][-4:] == '.jpg':
            jpg.append(files[i])
    return jpg

if __name__=='__main__':
    directory1 = r'C:\shkim\Year3\Group research project\dataset\test\rgb_resize'
    directory2 = r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\toGrey\sharpenFilt'
    #print(os.listdir(directory))
    files1 = os.listdir(directory1)
    files2 = os.listdir(directory2)
    
    file1 = jpgOnly(files1)
    file2 = jpgOnly(files2)
    print(file1,file2)
    for i in range(len(file1)):
        path1 = r'C:\shkim\Year3\Group research project\dataset\test\rgb_resize\\'
        path2 = r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\toGrey\sharpenFilt\\'
        image1 = path1+files1[i]
        image2 = path2+files2[i]
        a = str(i)+'.jpg'
        img_stitch(image1,image2,a)
    
