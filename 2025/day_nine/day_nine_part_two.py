import math
tiles = []
with open('day_nine/day_nine_data.txt') as f:
    for line in f:
        tiles.append(tuple(map(int, line.split(','))))
reds = set(tiles)
greens = set()

for i in range(len(tiles)):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i+1) % len(tiles)]

    if x1 == x2: 
        step = 1 if y2 > y1 else -1
        for y in range(y1 + step, y2, step):
            greens.add((x1, y))

    elif y1 == y2:
        step = 1 if x2 > x1 else -1
        for x in range(x1 + step, x2, step):
            greens.add((x, y1))

xs = [x for x, y in tiles]
ys = [y for x, y in tiles]
minx, maxx = min(xs), max(xs)
miny, maxy = min(ys), max(ys)

def inside(p, poly):
    x, y = p
    cnt = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i+1) % len(poly)]
        if min(y1, y2) < y <= max(y1, y2):
            x_at_y = x1 + (y - y1) * (x2 - x1) / (y2 - y1 + 1e-9)
            if x < x_at_y:
                cnt ^= 1
    return cnt == 1

inside_greens = set()

for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        if inside((x, y), tiles):
            inside_greens.add((x, y))

all_greens = greens.union(inside_greens).union(reds)

max_area = 0

for i in range(len(tiles)):
    x1, y1 = tiles[i]

    for j in range(i+1, len(tiles)):
        x2, y2 = tiles[j]

        width  = abs(x2 - x1) + 1
        height = abs(y2 - y1) + 1
        area = width * height

        if area < max_area:
            continue

        valid = True
        for x in range(min(x1,x2), max(x1,x2)+1):
            if not valid:
                break

            for y in range(min(y1,y2), max(y1,y2)+1):
                if (x, y) not in all_greens:
                    valid = False
                    break

        if valid:
            max_area = max(max_area, area)


print(max_area)
# pairs = []
# for i in range(len(tiles)):
#     for j in range(i + 1, len(tiles)):
#         pairs.append([(abs(tiles[i][0] - tiles[j][0])+1) * (abs(tiles[i][1]-tiles[j][1])+1), i, j])
# pairs.sort(key= lambda x:x[0], reverse=True)

# print(pairs)

