tiles = []

with open("day_nine/day_nine_data.txt") as file:
    for line in file:
        tiles.append([int(x) for x in line.strip().split(",")])

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def segments_intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    
def point_in_rectangle(point, first, second):
    x, y = point
    x1, y1 = min(first[0], second[0]), min(first[1], second[1])
    x2, y2 = max(first[0], second[0]), max(first[1], second[1])
    return x1 < x < x2 and y1 < y < y2

def intersecting(first, second):
    if first[0] == second[0] or first[1] == second[1]:
        return True
    
    x1, y1 = min(first[0], second[0]), min(first[1], second[1])
    x2, y2 = max(first[0], second[0]), max(first[1], second[1])
    
    corners = [
        (x1, y1),
        (x2, y1),
        (x2, y2),
        (x1, y2)
    ]
    if list(first) not in tiles or list(second) not in tiles:
        return True
    
    idx_first = tiles.index(list(first))
    idx_second = tiles.index(list(second))
    

    for i in range(len(tiles) - 1):
        if i == idx_first or i == idx_second or i + 1 == idx_first or i + 1 == idx_second:
            continue
            
        start = (tiles[i][0], tiles[i][1])
        end = (tiles[i+1][0], tiles[i+1][1])
        
        if point_in_rectangle(start, first, second):
            return True
        if point_in_rectangle(end, first, second):
            return True
        
        for j in range(4):
            edge_start = corners[j]
            edge_end = corners[(j + 1) % 4]
            
            if segments_intersect(edge_start, edge_end, start, end):
                return True
    
    return False

                
area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        # The biggest change is checking if it intersects ANY other line segment
        area = area if intersecting(tiles[i], tiles[j]) else max(area, (abs(tiles[i][0] - tiles[j][0])+1) * (abs(tiles[i][1] - tiles[j][1])+1))

print(area)