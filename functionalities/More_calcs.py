import numpy as np
import matplotlib.pyplot as plt
import math
import random

import Misc_function

def distr_between_midpoints(x1, y1, x2, y2, x3, y3, x4, y4):
    mid_1 = Misc_function.midpoint(x1, y1, x2, y2)
    mid_2 = Misc_function.midpoint(x3, y3, x4, y4)

    return Misc_function.distance_formula(mid_1[0], mid_1[1], mid_2[0], mid_2[1])

def if_angle_inside_ret_avg(x,y,z):
    if Misc_function.angle_inside(x,y,z):
       return Misc_function.angle_avg(x,y)

def in_circle(x, y, r,x_circle,y_circle):
    if(Misc_function.distance_formula(x,y,x_circle,y_circle)<=r):
        return True
    else:
        return False

