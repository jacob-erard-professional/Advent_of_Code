inputs = []
with open("day_one/day_one_data.txt", "r") as file: 
    for line in file: 
        ins = line.strip() 
        inputs.append([ins[:1], int(ins[1:])]) 
    num = 50 
    count = 0 
    for dir, rot in inputs: 
        if dir == "R":
            num += rot 
        else: 
            num -= rot
        num %= 100
        if num == 0:
            count += 1
print(count)
