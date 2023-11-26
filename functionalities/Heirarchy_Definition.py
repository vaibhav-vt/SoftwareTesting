import numpy as np
from .Misc_function import *



def define_heirarchy(levels, num_levels, line_levels):
    if(len(levels[0]) == 1):
        root = node(levels[0][0][2], levels[0][0][1])
    else:
        root = node(' ', 0)
    root.set_angRange((0, 360))
    nodes_dict = {}

    for i in range(1, num_levels+1):
        for ele in levels[i]:
            levels[i].sort(key=lambda x: x[1])

    # In the case where the sunburst chart has a root node at the center:
    if(len(levels[0]) == 1):

        for i in range(0, num_levels+1):
            nodes_dict[i] = []

        nodes_dict[0].append(root)

        for i in range(1, num_levels+1):
            for ele in levels[i]:
                nodes_dict[i].append(node(ele[2], ele[1]))

        for i in range(1, num_levels+1):
            for k in range(0, len(levels[i])):
                for j in range(0, len(line_levels[i])):
                    if(j == len(line_levels[i])-1):
                        if(angle_inside(line_levels[i][j][1], line_levels[i][0][1], levels[i][k][1])):
                            nodes_dict[i][k].set_angRange(
                                (line_levels[i][j][1], line_levels[i][0][1]))
                    else:
                        if(angle_inside(line_levels[i][j][1], line_levels[i][j+1][1], levels[i][k][1])):
                            nodes_dict[i][k].set_angRange(
                                (line_levels[i][j][1], line_levels[i][j+1][1]))

        # for i in range(0, num_levels+1):
        #     print(i, ' ')
        #     for ele in nodes_dict[i]:
        #         ele.print_node()

        for j in range(0, len(nodes_dict[1])):
            nodes_dict[1][j].set_parent(root)

        for i in range(0, num_levels):

            for j in range(0, len(nodes_dict[i])):

                for k in range(0, len(nodes_dict[i+1])):

                    if(nodes_dict[i][j].angle_range != None and nodes_dict[i+1][k].angle_range != None):
                        if(angle_inside(nodes_dict[i][j].angle_range[0], nodes_dict[i][j].angle_range[1], angle_avg(nodes_dict[i+1][k].angle_range[0], nodes_dict[i+1][k].angle_range[1]))):
                            nodes_dict[i+1][k].set_parent(nodes_dict[i][j])

        for i in range(0, num_levels+1):
            for ele in nodes_dict[i]:
                if(ele.parent != None):
                    nd = ele.parent
                    nd.set_children(ele)
        # print('THE TREE HAS THE FOLLOWING NODES')
        # for i in range(0, num_levels+1):
        #     print(i, ' ')
        #     for ele in nodes_dict[i]:
        #         ele.print_node()

        # print(root)

    # In the case where the sunburst chart doesn't have a root node at the center:
    else:

        for i in range(-1, num_levels+1):
            nodes_dict[i] = []
        nodes_dict[-1].append(root)

        for i in range(0, num_levels+1):
            for ele in levels[i]:
                nodes_dict[i].append(node(ele[2], ele[1]))

        for i in range(0, num_levels+1):
            for k in range(0, len(levels[i])):
                for j in range(0, len(line_levels[i])):
                    if(j == len(line_levels[i])-1):
                        if(angle_inside(line_levels[i][j][1], line_levels[i][0][1], levels[i][k][1])):
                            nodes_dict[i][k].set_angRange(
                                (line_levels[i][j][1], line_levels[i][0][1]))
                    else:
                        if(angle_inside(line_levels[i][j][1], line_levels[i][j+1][1], levels[i][k][1])):
                            nodes_dict[i][k].set_angRange(
                                (line_levels[i][j][1], line_levels[i][j+1][1]))

        for j in range(0, len(nodes_dict[0])):
            nodes_dict[0][j].set_parent(root)

        for i in range(-1, num_levels):
            for j in range(0, len(nodes_dict[i])):
                for k in range(0, len(nodes_dict[i+1])):
                    if(nodes_dict[i][j].angle_range != None and nodes_dict[i+1][k].angle_range != None):
                        if(angle_inside(nodes_dict[i][j].angle_range[0], nodes_dict[i][j].angle_range[1], angle_avg(nodes_dict[i+1][k].angle_range[0], nodes_dict[i+1][k].angle_range[1]))):
                            nodes_dict[i+1][k].set_parent(nodes_dict[i][j])

        # constructing the tree
        for i in range(-1, num_levels+1):
            for ele in nodes_dict[i]:
                if(ele.parent != None):
                    nd = ele.parent
                    nd.set_children(ele)
        # Printing the tree
        # print('THE TREE HAS THE FOLLOWING NODES')
        # for i in range(-1, num_levels+1):
        #     print(i, ' ')
        #     for ele in nodes_dict[i]:
        #         ele.print_node()

        # print(root)

    return nodes_dict,root
