import cv2
import numpy as np
import math
from Circle_Detection import *
from Misc_function import *

def draw_lines(cdstP, accepted_lines):
    if accepted_lines is not None:
        for i in accepted_lines:
            cv2.line(cdstP, (i[0][0], i[0][1]),
                     (i[1][0], i[1][1]), (0, 0, 255), 1, cv2.LINE_AA)

def set_lines_angles(accepted_lines,x_circle,y_circle):
    lines_angles = []
    if accepted_lines is not None:
        for i in accepted_lines:
            lines_angles.append(angle_formula(
                i[0][0], i[0][1], i[1][0], i[1][1],x_circle,y_circle))
    return lines_angles

def define_line_levels(accepted_lines,levels,x_circle,y_circle):
    level_radius = []
    for i in levels.keys():
        level_radius.append(levels[i][0][0])

    line_levels = {}
    for i in range(0, len(level_radius)):
        line_levels[i] = []

    for i in range(0, len(level_radius)):
        for j in accepted_lines:
            if((in_circle(j[0][0], j[0][1], level_radius[i],x_circle,y_circle) == True and in_circle(j[1][0], j[1][1], level_radius[i],x_circle,y_circle) == False) or (in_circle(j[0][0], j[0][1], level_radius[i],x_circle,y_circle) == False and in_circle(j[1][0], j[1][1], level_radius[i],x_circle,y_circle) == True)):
                line_levels[i].append(
                    [j, angle_formula(j[0][0], j[0][1], j[1][0], j[1][1],x_circle,y_circle)])

    for i in line_levels:
        for j in line_levels[i]:
            line_levels[i].sort(key=lambda x: x[1])
    return line_levels, level_radius

def filter_lines(lines,x_circle,y_circle):
    accepted_lines = []
    for i in lines:
        x1 = int(i[0][0])
        y1 = int(i[0][1])
        x2 = int(i[1][0])
        y2 = int(i[1][1])
        d1 = abs((y2-y1)*x_circle - (x2-x1) *
                 y_circle - (y2-y1)*x1 + (x2-x1)*y1)
        d2 = math.sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))
        d3 = d1/d2
        if d3 <= 20:
            accepted_lines.append([(x1, y1), (x2, y2)])

    return accepted_lines

def del_redundant_lines(line_levels):
    for i in line_levels:
        rem_ind = []
        for j in line_levels[i]:
            for k in line_levels[i]:
                if(k != j):
                    if(abs(k[1]-j[1]) < 3.5):
                        if(distance_formula(k[0][0][0], k[0][0][1], k[0][1][0], k[0][1][1]) < distance_formula(j[0][0][0], j[0][0][1], j[0][1][0], j[0][1][1])):
                            rem_ind.append(k)
                        elif(distance_formula(k[0][0][0], k[0][0][1], k[0][1][0], k[0][1][1]) == distance_formula(j[0][0][0], j[0][0][1], j[0][1][0], j[0][1][1])):
                            line_levels[i].remove(k)
        for m in rem_ind:
            if(m in line_levels[i]):
                line_levels[i].remove(m)

    return line_levels


def detect_lines(img_no_text, levels,x_circle,y_circle):

    
    # Doing Basic image pre-processing to prepare the image for line detection
    img_no_text = cv2.cvtColor(img_no_text,cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(img_no_text, (4,4))
    dst = cv2.Canny(blur, 25, 100, None, 3)
    cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
    cdstP = np.copy(cdst)

    # Using probabilistic Hough Transform to Detect lines
    linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 30, None, 20, 30)

    lines = []
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            lines.append([[l[0], l[1]], [l[2], l[3]]])
    # Filtering out a few redundant lines 

    accepted_lines = filter_lines(lines,x_circle,y_circle)

    draw_lines(cdstP, accepted_lines)

    # defining the angle range in which the line line
    lines_angles = set_lines_angles(accepted_lines,x_circle,y_circle)

    # Defining a rudimentary Heirarchy in the lines
    line_levels,level_radius = define_line_levels(accepted_lines,levels,x_circle,y_circle)

    # Removing a few redundant lines, if the perpendicular dist b/w them is <3.5
    line_levels = del_redundant_lines(line_levels)

    cdst1 = np.copy(blur)
    for i in line_levels:
        for j in line_levels[i]:
            cv2.line(cdst1, (j[0][0][0], j[0][0][1]), (j[0][1]
                     [0], j[0][1][1]), (0, 255, 255), 3, cv2.LINE_AA)

    return line_levels, cdst1, level_radius
