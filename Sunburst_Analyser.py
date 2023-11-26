import cv2
import matplotlib.pyplot as plt
import keras_ocr
import pprint
from zss import Node
import csv

# from functionalities.Circle_Detection import x_circle,y_circle
from functionalities.Text_Detection import detect_text
from functionalities.Text_Removal import inpaint_text
from functionalities.Circle_Detection import detect_circles
from functionalities.Line_Detection import detect_lines
from functionalities.Heirarchy_Definition import define_heirarchy
from functionalities.Misc_function import make_csv

if __name__ == "__main__":

    
    # Reading the input image
    pipeline = keras_ocr.pipeline.Pipeline()
    print('Enter the name of the input image: ')
    image_name = input()
    orignal_img = cv2.imread(image_name)

    # Removing text from the image:
    notext_img = inpaint_text(orignal_img,pipeline)
    cv2.imshow('No Text Image.png',notext_img)
    rgb_img = cv2.cvtColor(notext_img,cv2.COLOR_BGR2RGB)
    bw_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("black_white image.png",bw_img)
    # Detecting Circles in the Image
    circle_img, x_circle, y_circle = detect_circles(bw_img)
    cv2.imshow("circle detection",circle_img)

    # Detecting the text in the image
    # print(x_circle,y_circle)

    text_levels, num_levels = detect_text(orignal_img,pipeline,x_circle,y_circle)
    print('BELOW IS THE DETECTED TEXT WITH RUDIMENTARY LEVELS ASSIGNED:')
    pprint.pprint(text_levels)

    # Detecting Lines in the image
    line_levels, lines_img, level_radius = detect_lines(notext_img, text_levels,x_circle,y_circle)
    print('BELOW ARE THE DETECTED LINES WITH RUDIMENTARY LEVELS ASSIGNED:')
    pprint.pprint(line_levels)  
    cv2.imshow("sector boundaries",lines_img)

    # Hierarchy Definition
    nodes_dict,root = define_heirarchy(text_levels, num_levels, line_levels)
    print(root)
    # pprint.pprint(nodes_dict)

    # Making an output CSV of the extracted data in heirarchial data format
    # print("Enter the name of the output CSV file containing the extracted data:")
    # csv_name = input()
    # make_csv(nodes_dict,csv_name)

cv2.waitKey(0)
cv2.destroyAllWindows()





    