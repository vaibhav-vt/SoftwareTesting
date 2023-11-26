from functionalities.Misc_function import make_csv, node
from functionalities.Heirarchy_Definition import define_heirarchy
from functionalities.Line_Detection import detect_lines
from functionalities.Circle_Detection import detect_circles
from functionalities.Text_Removal import inpaint_text
from functionalities.Text_Detection import detect_text
import pprint
from zss import Node
import keras_ocr
import matplotlib.pyplot as plt
import cv2
from tqdm import tqdm
import os
import math
import csv
from zss import simple_distance, distance
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# import pprint


def insert_cost(node):
    return 1


def remove_cost(node):
    return 1


def update_cost(a,b):
    return 0

def insert_cost2(node):
    return 0


def remove_cost2(node):
    return 0


def update_cost2(a,b):
    return 1

def get_children(node):
    return node.children


def make_zss(labels, parents):
    nodes_lst = {}
    nodes_parents = []
    for i in range(len(labels)):
        nodes_lst[labels[i]] = Node(labels[i])
        nodes_parents.append((labels[i], parents[i]))
    for ele in nodes_parents:
        if(ele[1] != ''):
            nodes_lst[ele[1]].addkid(nodes_lst[ele[0]])
    return nodes_lst

node_lst =[]
def make_node_arrays(root):
     
    for ele in root.children:
          make_node_arrays(ele)
    node_lst.append(root)
 
     


def make_plot_arrays():
    nodes = []
    parents = []
    for i in node_lst:
        if(i.parent == None):
            nodes.append(i.text)
            parents.append('')
    for i in node_lst:
        if(i.parent != None):
            nodes.append(i.text)
            parents.append(i.parent.text)

    return nodes, parents


def get_original_arrays(image_name, filename,code):
    df_category = pd.read_excel(filename)
    dict_category = df_category.set_index('Image Name').T.to_dict('list')
    size1 = len(dict_category[image_name][0])
    labels = dict_category[image_name][0][1:size1-1].split(',')
#   print(dict_category)
    size2 = len(dict_category[image_name][1])
    parents = dict_category[image_name][1][1:size2-1].split(',')
    if(code == 'R'):
        for i in range(len(labels)):
            if(i==0):
                    labels[i] = labels[i][1:5]
            else:
                labels[i] = labels[i][2:6]
        for i in range(len(parents)):
            if(i==0):
                    parents[i] = ''
            else:
                parents[i] = parents[i][2:6]
    if(code == 'H'):
        for i in range(len(labels)):
            if(i==0):
                    labels[i] = labels[i][1:2]
            else:
                labels[i] = labels[i][2:6]
        for i in range(len(parents)):
            if(i==0):
                    parents[i] = ''
            elif(parents[i]==" ' '"):
                    parents[i]=' '
            else:
                parents[i] = parents[i][2:6]

    return labels, parents


TEST_DIR = 'validation\Validation_Dataset\ROOT_SHALLOW'
excel_sheet = 'Original_RS.xlsx'
# Total_categories = ['\HOLLOW_DEEP','\HOLLOW_SHALLOW','\ROOT_DEEP','\ROOT_SHALLOW']

path2 = os.path.join(TEST_DIR, excel_sheet)
file_obj = open("root_shallow.txt", "w")
file_obj.write('Image name, SS, DS, TS\n')
for img in tqdm(os.listdir(TEST_DIR)):
    if(img[0:2] =='RS'):
        print(img)
        path = os.path.join(TEST_DIR, img)
        pipeline = keras_ocr.pipeline.Pipeline()
        orignal_img = cv2.imread(path)
        # Removing text from the image:
        notext_img = inpaint_text(orignal_img, pipeline)

        rgb_img = cv2.cvtColor(notext_img, cv2.COLOR_BGR2RGB)
        bw_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2GRAY)

        # Detecting Circles in the Image
        circle_img, x_circle, y_circle = detect_circles(bw_img)


        # Detecting the text in the image
        text_levels, num_levels = detect_text(
            orignal_img, pipeline, x_circle, y_circle)

        # Detecting Lines in the image
        line_levels, lines_img, level_radius = detect_lines(
            notext_img, text_levels, x_circle, y_circle)
 

        # Hierarchy Definition
        nodes_dict, root = define_heirarchy(
            text_levels, num_levels, line_levels)
        print(root)
        make_node_arrays(root)
        # for ele in node_lst:
        #      print(ele.text, end=' ')
        # making tree structure arrays of original and extracted tree
        nodes_ex, parents_ex = make_plot_arrays()
        nodes_or, parents_or = get_original_arrays(img, path2,'R')
        # print(nodes_or)
        # print(parents_or)
        # print()
        # print(nodes_ex)
        # print(parents_ex)

        tree_ex = make_zss(nodes_ex, parents_ex)
        root_ex = Node('')
        for i in range(len(nodes_ex)):
            if(parents_ex[i] == ''):
                root_ex = tree_ex[nodes_ex[i]]
        # print(nodes_or,parents_or)
        tree_or = make_zss(nodes_or, parents_or)
        root_or = Node('')
        for i in range(len(nodes_or)):
            if(parents_or[i] == ''):
                root_or = tree_or[nodes_or[i]]

        for key in tree_ex:
            tree_ex[key].children.sort(key=lambda x: x.label)

        for key in tree_or:
            tree_or[key].children.sort(key=lambda x: x.label)

        ted_s = distance(root_ex, root_or, get_children=get_children, insert_cost=insert_cost, remove_cost=remove_cost, update_cost=update_cost)
        ted_d = distance(root_ex, root_or, get_children=get_children, insert_cost=insert_cost2, remove_cost=remove_cost2, update_cost=update_cost2)


        ss = math.sqrt(1/(1+ted_s))
        ds = math.sqrt(1/(1+ted_d))
        ss =round(ss,2)
        ds=round(ds,2)
        ts = 0.9*ss + 0.1*ds
        ts = round(ts,2)
        print(ss," ",ds, "", ts)
        line = img + ", "+ str(ss)+", " + str(ds) + ", " + str(ts)+'\n'

        file_obj.write(line)
        node_lst =[]