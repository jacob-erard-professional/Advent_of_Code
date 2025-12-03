inputs = []
with open("day_three/day_three_data.txt", "r") as file: 
    for line in file: 
        inputs.append(line.strip())

count = 0
for input in inputs:
    largest = input[-2:]
    for i in range(len(input)-3, -1, -1):
        if int(input[i]) >= int(largest[0]):
            old = largest[0]
            largest = input[i] + largest[1:]
            if int(old) > int(largest[1]):
                largest = largest[0] + old
                    
    count += int(largest)
print(count)