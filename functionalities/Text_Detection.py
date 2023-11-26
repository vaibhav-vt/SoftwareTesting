from .Misc_function import *
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
def levelize(dist_array):
    # initialize levels
    levels = {}
    num_levels = 0
    for i in range(len(dist_array)-1):
        if(abs(dist_array[i][0]-dist_array[i+1][0]) >= 20):
            num_levels += 1

    for i in range(num_levels+1):
        levels[i] = []

    # classify all text locations on basis of dist. from centre into levels
    flag = 0
    for i in range(len(dist_array)-1):
        if(i == len(dist_array)-2):
            if(abs(dist_array[i][0]-dist_array[i+1][0]) <= 20):
                levels[flag].append(dist_array[i])
                levels[flag].append(dist_array[i+1])
            else:
                levels[flag].append(dist_array[i])
                flag += 1
                levels[flag].append(dist_array[i+1])

        elif(abs(dist_array[i][0]-dist_array[i+1][0]) <= 20):
            levels[flag].append(dist_array[i])
        else:
            levels[flag].append(dist_array[i])
            flag += 1

    return levels, num_levels


def detect_text(img, pipeline, x_circle, y_circle):
    # get height and width
    height = img.shape[0]
    width = img.shape[1]

    # initiaize dicts and arrays
    cordi_dict1 = {}
    dist_dict1 = {}
    dist_array1 = []

    # get text box centroid(text location) and store in cordi_dict
    prediction_groups = pipeline.recognize([img])
    for i in prediction_groups[0]:
        x_cordi = (i[1][0][0]+i[1][1][0]+i[1][2][0]+i[1][3][0])/4
        y_cordi = (i[1][0][1]+i[1][1][1]+i[1][2][1]+i[1][3][1])/4
        cordi_dict1[i[0]] = (round(x_cordi), round(y_cordi))

    x = sorted(cordi_dict1.items(), key=lambda x: x[1][0])
    cordi_dict1 = dict(x)

    # calculate dist, angle for each text
    for key, values in cordi_dict1.items():
        dist_dict1[key] = round(distance_formula(
            values[0], values[1], x_circle, y_circle))
        dist_array1.append((round(distance_formula(values[0], values[1], x_circle, y_circle)),angle_formula(
            values[0], values[1], x_circle, y_circle,x_circle, y_circle), key))

    # sort by distance
    dist_array1.sort(key=lambda tup: tup[0])

    # initialize levels to the detected text
    levels1, num_levels = levelize(dist_array1)

    return levels1, num_levels
