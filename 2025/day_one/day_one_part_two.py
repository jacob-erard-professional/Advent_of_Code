inputs = []
with open("day_one/day_one_data.txt", "r") as file: 
    for line in file: 
        ins = line.strip() 
        inputs.append([ins[:1], int(ins[1:])]) 
    num = 50 
    count = 0 
    for dir, rot in inputs: 
        curr = num 
        if dir == "R":
            num += rot 
            count += num//100
        else: 
            num -= rot 
            if curr == 0:
                count += abs(num)//100
            else:
                count += (abs(num)//100 + 1) if num < 0 else 0
            if num == 0:
                count += 1
        num %= 100
print(count)
