import cv2
import shutil
import os
import numpy as np

basepath = "./pictures/"

for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        #print(entry)
        img_path = basepath+entry
        dest_path = "./blurry_pics"
        #print(img_path)
        img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
        laplace_var = cv2.Laplacian(img,cv2.CV_64F).var()
        if laplace_var<5:
            print(entry+" has been moved")
            shutil.move(img_path,dest_path)


