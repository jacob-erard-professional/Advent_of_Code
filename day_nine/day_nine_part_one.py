tiles = []

with open("day_nine/day_nine_data.txt") as file:
    for line in file:
        tiles.append([int(x) for x in line.strip().split(",")])

area = 0
for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        area = max(area, (abs(tiles[i][0] - tiles[j][0])+1) * (abs(tiles[i][1] - tiles[j][1])+1))

print(area)