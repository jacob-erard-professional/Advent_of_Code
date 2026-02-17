tiles = []
with open('day_nine/day_nine_data.txt') as f:
    for line in f:
        tiles.append(list(map(int, line.split(','))))
        
area = 0
for i in range(len(tiles)):
    for j in range(i+1, len(tiles)):
        area = max(area, (abs(tiles[i][0] - tiles[j][0])+1) * (abs(tiles[i][1]-tiles[j][1])+1))
print(area)