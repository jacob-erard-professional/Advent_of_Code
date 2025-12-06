import numpy as np
arr = []
with open('day_six/day_six_data_one.txt') as f:
    arr = [line.rstrip('\n') for line in f]
        
ops = []
with open('day_six/day_six_data_two.txt') as f:
    for line in f:
        ops = line.split()

count = 0
op_num = len(ops) -1
temp = np.array([])
num = ""
for i in reversed(range(0, len(arr[0]))):
    for j in range(len(arr)):
        if arr[j][i] != " ":
            num += arr[j][i]
    if num != "":
        temp = np.append(temp, num)
        num = ""
    elif num == "" or i==0:
        if ops[op_num] == '+':
            count += (temp.astype(int).sum())
        else:
            count += (temp.astype(int).prod())
        op_num -= 1
        temp = np.array([])
if ops[op_num] == '+':
    count += (temp.astype(int).sum())
else:
    count += (temp.astype(int).prod())
op_num -= 1
temp = np.array([])

    
print(count)
