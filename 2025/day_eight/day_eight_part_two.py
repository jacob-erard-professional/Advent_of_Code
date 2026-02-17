import heapq
import math
"""
This code was adapted from my implementation in CS4150
"""
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, component_size, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if component_size[root_x] > component_size[root_y]:
            component_size[root_x] += component_size[root_y]
            parent[root_y] = root_x
        elif component_size[root_x] < component_size[root_y]:
            component_size[root_y] += component_size[root_x]
            parent[root_x] = root_y
        else:
            parent[root_x] = root_y
            component_size[root_y] *= 2

def min_cable_length(coordinates, parent, component_size):
    edges = []

    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            dist = math.dist(coordinates[i], coordinates[j])
            heapq.heappush(edges, (dist, i, j))

    while len(set(parent)) > 1:
        _, v1, v2 = heapq.heappop(edges)
        if find(parent, v1) != find(parent, v2):
            union(parent, component_size, v1, v2)
            print(coordinates[v1], coordinates[v2])        


with open('day_eight/day_eight_data.txt') as f:           
    coordinates = [tuple(map(float, line.split(','))) for line in f]
     
parent = list(range(1000))
component_size = [1]*1000


min_cable_length(coordinates, parent, component_size)