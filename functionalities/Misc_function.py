
import numpy as np
import matplotlib.pyplot as plt
import math
# from .Circle_Detection import x_circle, y_circle
import csv

def calc_percentage(range):
    if((range[1]-range[0]) > 0):
        percentage = (range[1]-range[0])/360*100
    else:
        percentage = (range[1]-range[0]+360)/360*100
    return percentage


def midpoint(x1, y1, x2, y2):
    x_mid = int((x1 + x2)/2)
    y_mid = int((y1 + y2)/2)
    return (x_mid, y_mid)


def distance_formula(x1, y1, x2, y2):
    dist = math.sqrt(pow(x1-x2, 2)+pow(y1-y2, 2))
    return dist


def in_circle(x, y, r,x_circle,y_circle):
    if((x-x_circle)**2 + (y-y_circle)**2 - r**2 <= 0):
        return True
    else:
        return False


def angle_formula(x1, y1, x2, y2,x_circle,y_circle):
    if (x2-x1) == 0:
        if y1 > y_circle:
            return 270
        else:
            return 90

    else:
        ang = math.atan((y1-y2)/(x2-x1))*180/math.pi

        if x1 < x_circle:
            ang += 180
        if x1 > x_circle and ang < 0:
            ang += 360

    return ang


def proximity(x, y, z, d):
    if(abs(x-y) <= d or abs(y-z) <= d or abs(x-z) <= d):
        return True
    return False


# def choose_best(k1, k2, k3):
#     if(k1 == k2):
#         return k1
#     if(k2 == k3):
#         return k2
#     if(k3 == k1):
#         return k3
#     if(len(k1) >= len(k2) and len(k1) >= len(k3)):
#         return k1
#     if(len(k2) > len(k1) and len(k2) > len(k3)):
#         return k2
#     if(len(k3) > len(k1) and len(k3) > len(k2)):
#         return k3


def angle_inside(x, y, z):
    if(x > y):
        if(z > x and z <= 360):
            return True
        if(z < y and z >= 0):
            return True
    else:
        if(z > x and z < y):
            return True
    return False


def angle_avg(x, y):
    if(x <= y):
        return (x+y)/2
    else:
        diff = ((360-x)+y)/2
        if(y-diff < 0):
            return 360+(y-diff)
        else:
            return y-diff


# def make_csv(nodes_dict,name):
#     lst_nodes = []
#     for i in nodes_dict:
#         for ele in nodes_dict[i]:
#             lst_nodes.append(ele)

#     print(len(lst_nodes))

#     fieldname = ['Value', 'Parent']
#     rows = []
#     for i in lst_nodes:
#         temp_dict = {}
#         temp_dict['Value'] = i.text
#         # temp_dict['Percentage of graph']=i.percentage
#         if(i.parent != None):
#             temp_dict['Parent'] = i.parent.text
#         else:
#             temp_dict['Parent'] = 'No parent, is root node'
#         rows.append(temp_dict)

#     with open(name, 'w', encoding='UTF8', newline='') as f:
#         writer = csv.DictWriter(f, delimiter='|', fieldnames=fieldname)
#         writer.writeheader()
#         writer.writerows(rows)



# class node:
#     def __init__(self, text, txt_angle):
#         self.text = text
#         self.text_angle = txt_angle
#         self.parent = None
#         self.children = []
#         self.angle_range = None
#         self.percentage = None

#     def set_angRange(self, range):
#         self.angle_range = range
#         self.percentage = calc_percentage(range)

#     def createNode(self, text, txt_angle, angle_range):
#         return node(text, txt_angle, angle_range)

#     def print_node(self):
#         if(self.parent == None):
#             print('node: ', self.text, ' ', self.text_angle,
#                   ' ', self.angle_range, ' ', self.children)
#         else:
#             print('node: ', self.text, ' ', self.text_angle, ' ',
#                   self.angle_range, ' ', self.parent.text, ' ', self.percentage)

#     def set_children(self, child):
#         self.children.append(child)

#     def set_parent(self, prnt):
#         self.parent = prnt

#     def __repr__(self, level=0):
#         ret = "\t"*level+repr(self.text)+" : "+repr(self.percentage)+"\n"
#         for child in self.children:
#             ret += child.__repr__(level+1)
#         return ret
