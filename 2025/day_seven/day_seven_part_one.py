lines = []
with open('day_seven/day_seven_data.txt') as f:
    for line in f:
        lines.append(list(line.strip()))

start = lines[0].index('S')

spliticies = {start}
count = 0
for i in range(2, len(lines), 2):
    temp = set()
    remove = set()
    for index in spliticies:
        if lines[i][index] == "^":
            remove.add(index)
            temp.add(index + 1)
            temp.add(index - 1)
            count += 1
    spliticies = temp.union(spliticies).difference(remove)
    
print(count)
