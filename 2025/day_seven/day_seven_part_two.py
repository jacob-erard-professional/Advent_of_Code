lines = []
with open('day_seven/day_seven_data.txt') as f:
    for line in f:
        lines.append(list(line.strip()))
lines.append([0]  * len(lines[0]))

for i in reversed(range(2, len(lines)-2, 2)):
    for index, sym in enumerate(lines[i]):
        if sym == '^':
            lines[i][index] = lines[i+2][index+1] + lines[i+2][index-1] + 1
        else: lines[i][index] = lines[i+2][index]

    
print(max(lines[2]) + 1)
