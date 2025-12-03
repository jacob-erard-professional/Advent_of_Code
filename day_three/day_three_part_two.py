inputs = []
with open("day_three/day_three_data.txt", "r") as file: 
    for line in file: 
        inputs.append(line.strip())

count = 0
for input in inputs:
    largest = input[-12:]
    for i in range(len(input)-13, -1, -1):
        if int(input[i]) >= int(largest[0]):
            old = largest[0]
            largest = input[i] + largest[1:]
            for j in range(1,12):
                if int(old) >= int(largest[j]):
                    temp = largest[j]
                    largest = largest[:j] + old + largest[j+1:]
                    old = temp
                else: break
                    
    count += int(largest)
print(count)