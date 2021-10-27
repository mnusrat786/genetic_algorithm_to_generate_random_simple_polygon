from shapely.geometry import LineString
import numpy as np
import matplotlib.pyplot as plt
import random

list_of_points = [[0.2,1.2],[1.4,1.4],[1.6,2.5],[0.8,2.4],[0.0,4.0],[3.0,1.0],[0.5,0.5]]
random.shuffle(list_of_points)
print(list_of_points)

p0,p1,p2,p3,p4,p5,p6 = list_of_points 

def plot_chain(list_of_points):
    """
    Args:
        list of lists: [[x1,y1],[x2,y2]...[xn,yn]]
    Returns:
        None
    """
    x,y = np.array(list_of_points).T
    plt.plot(x,y)
    plt.show()
plot_chain(list_of_points)

def check_intersect_lines(l1,l2):
    """
    Args: 
        l1,l2: list of start & end x,y pairs
    Returns:
        bool: whether the lines intersect or not
    """
    line1 = LineString([l1[0],l1[1]])
    line2 = LineString([l2[0],l2[1]])
    xy = [i for i in line1.intersection(line2).coords]

    if xy:
        if list(xy[0]) in l1:
            return False
        else:
            return True
    else:
        return False

check_intersect_lines([p1,p3],[p1,p5])

def calculate_intersections(list_of_points):
    intersections = 0
    for i in range(len(list_of_points)-2):

        l1 = [list_of_points[i],list_of_points[i+1]]
        for j in range(i+1,len(list_of_points)-1):

            l2 = [list_of_points[j],list_of_points[j+1]]
            if check_intersect_lines(l1,l2):
               
                intersections += 1
    return intersections

calculate_intersections(list_of_points)

def get_chain(list_of_points):
    fitness = calculate_intersections(list_of_points)
    while fitness != 0:
        
        plot_chain(list_of_points)
        random.shuffle(list_of_points)
        fitness = calculate_intersections(list_of_points)
    plot_chain(list_of_points)
    
    return list_of_points

list_of_points = get_chain(list_of_points)

def get_fitness(list_of_points):
    f, l = [list_of_points[0],list_of_points[-1]]
    l1 = [f, l]
    B = []
    fitness = 0
    for i in range(0,len(list_of_points)-1):
        l2 = [list_of_points[i],list_of_points[i+1]]
        if check_intersect_lines(l1,l2):
            B.append(l2)
            fitness += 1
    return B, fitness

B, fitness = get_fitness(list_of_points)
B, fitness

def modify_chain(B, list_of_points):
    plot_chain(list_of_points)
    r = random.randint(0,len(B)-1)
    m, n = B[r]
    x, y = [list_of_points[0],list_of_points[-1]]
    list1 = list_of_points[0:list_of_points.index(m)+1][::-1]
    list2 = list_of_points[list_of_points.index(m)+1:]
    list_of_points = [*list1, *list2]
    plot_chain(list_of_points)
    return list_of_points

modify_chain(B, list_of_points)

B, fitness = get_fitness(list_of_points)
while fitness != 0:
    list_of_points = modify_chain(B, list_of_points)
    B, fitness = get_fitness(list_of_points)
    print(fitness)
list_of_points.append(list_of_points[0])
plot_chain(list_of_points)


    