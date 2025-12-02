import csv
with open("day_two/day_two.txt", "r") as file:
    csv_reader = csv.reader(file)
    row = next(csv_reader) 
    inputs = [list(map(int, field.split('-'))) for field in row]
total = 0
for input in inputs:
    for i in range(input[0], input[1] + 1):
        string = str(i)
        for j in range(1, len(string)//2 + 1):
            pattern = string[:j]
            if pattern * (len(string) // j) == string:
                print(i)
                total += i
                break
print(total)
