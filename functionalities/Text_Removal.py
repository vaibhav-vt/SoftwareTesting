import cv2
import numpy as np
import keras_ocr
import math
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from .Misc_function import *

def inpaint_text(img_path, pipeline):
    # read image
    img = keras_ocr.tools.read(img_path)

    # generate (word, box) tuples 
    prediction_groups = pipeline.recognize([img])
    mask = np.zeros(img.shape[:2], dtype="uint8")

    #for each detected text
    for box in prediction_groups[0]:
        x0, y0 = box[1][0]
        x1, y1 = box[1][1] 
        x2, y2 = box[1][2]
        x3, y3 = box[1][3] 
        #each mid pt of sides of textbox
        x_mid0, y_mid0 = midpoint(x0, y0, x1, y1)
        x_mid1, y_mid1 = midpoint(x1, y1, x2, y2)
        x_mid2, y_mid2 = midpoint(x2, y2, x3, y3)
        x_mid3, y_mid3 = midpoint(x3, y3, x0, y0)

        x_mid=0 
        y_mid=0
        x_mid_=0 
        y_mid_=0
        
        #max length line
        if(distance_formula(x_mid0,y_mid0,x_mid2,y_mid2) >= distance_formula(x_mid1,y_mid1,x_mid3,y_mid3)):
          x_mid, y_mid = (x_mid0,y_mid0)
          x_mid_, y_mid_ = (x_mid2,y_mid2)
        else:
          x_mid, y_mid = (x_mid1,y_mid1)
          x_mid_, y_mid_ = (x_mid3,y_mid3)

        thickness1 = int(math.sqrt( (x1 - x0)**2 + (y1 - y0)**2 ))
        thickness2 = int(math.sqrt( (x2 - x0)**2 + (y2 - y0)**2 ))
        thickness3 = int(math.sqrt( (x3 - x0)**2 + (y3 - y0)**2 ))

        #min thickness line
        thickness = min(thickness1, thickness2, thickness3)
        
        #plot line in the mask
        cv2.line(mask, (x_mid, y_mid), (x_mid_, y_mid_), 255, thickness)
        
        #inpaint mask over input
        img = cv2.inpaint(img, mask, 7, cv2.INPAINT_NS)
    
    return(img)