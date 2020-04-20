import flirimageextractor as flir
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import shutil
import sys
sys.path.insert(1,r'C:\shkim\Year3\Group research project\TIPA\TIPA_library\main')
from thermal_image_processing import optimal_quantization

#A function extracting the FLIR image 
def imageExtract(path,filename):
    f = flir.FlirImageExtractor()
    f.process_image(path)
    img = f.extract_thermal_image()
    result = optimal_quantization(img)
    cv2.imwrite(r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\\'+filename,result)
    path = r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\\'+filename
    toGrey(path,filename)

#A function to convert the image into a greyscale
def toGrey(path,filename):
    image = cv2.imread(path)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\toGrey\\'+filename, image_gray)
    sharpenFilt(image_gray,filename)

#A funcation to sharpen the edges since the thermal images are blurry on the edges
def sharpenFilt(src,filename):
    kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    result = cv2.filter2D(src,-1,kernel)
    cv2.imwrite(r'C:\shkim\Year3\Group research project\dataset\test\imageExtract\toGrey\sharpenFilt\\'+filename,result)

#Resize the rgb image so that it is same size as the thermal
def rgb_resize(src,scale,filename):
    src = cv2.imread(src)
    image = src[185:-90,120:-86]
    width = int(image.shape[1]* scale/100)
    height = int(image.shape[0]* scale/100)
    dim = (width,height)
    dst = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(r'C:\shkim\Year3\Group research project\dataset\test\rgb_resize\\'+filename,dst)

#Only pick out .jpg files 
def jpgOnly(files):
    jpg = []
    for i in range(len(files)):
        if files[i][-4:] == '.jpg':
            jpg.append(files[i])
    return jpg

#Main function
if __name__=='__main__':
    directory = r'C:\shkim\Year3\Group research project\dataset'
    print(os.listdir(directory))
    files = os.listdir(directory)
    
    file = jpgOnly(files)
    for i in range(len(file)):
        path = r'C:\shkim\Year3\Group research project\dataset\\'
        path = path + str(file[i])
        filename = str(i)+'.jpg'
        imageExtract(path,filename)
        scale = 55
        rgb_resize(path,scale,filename)
#gives an error(input file does not exist) if path is not assigned inside the
#for loop
#jpgOnly = []
#for i in range(len(files)):
#    if files[i][-4:] == '.jpg':
#        jpgOnly.append(files[i])

        
#for i in jpgOnly:
#    path = r'C:\shkim\Year3\Group research project\dataset\\'
#    path = path+i
#    imageExtract(path)

#files2 = os.listdir(directory)
#path = r'C:\shkim\Year3\Group research project\dataset\test\raw_data\\'
#dest = r'C:\shkim\Year3\Group research project\dataset\test\raw_data\new'
#for i in range(len(files2)):
#    if files2[i][-12:] == 'gnuplot2.jpg':
#        image = path + files2[i]
#        shutil.move(image,dest)

#new_path = r'C:\shkim\Year3\Group research project\dataset\test\raw_data\new'
#name = r'C:\shkim\Year3\Group research project\dataset\test\raw_data\new\\'
#files3 = os.listdir(new_path)
#jpgOnly = []
#for i in range(len(files3)):
#    if files3[i][-4:] == '.jpg':
#        jpgOnly.append(files3[i])

#for i in range(len(jpgOnly)):
#    src = name + str(jpgOnly[i])
#    dst = name + str(i) + '.jpg'
#    dst2 = name + str(i) + '_sharpen.jpg'
#    toGrey(src,dst,dst2)
