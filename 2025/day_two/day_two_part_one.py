import csv
with open("day_two/day_two.txt", "r") as file:
    csv_reader = csv.reader(file)
    row = next(csv_reader) 
    inputs = [list(map(int, field.split('-'))) for field in row]
total = 0
for input in inputs:
    for i in range(input[0], input[1] + 1):
        if str(i).startswith(str(i)[len(str(i))//2:]) and len(str(i)) %2 == 0:
            total+=i
print(total)
