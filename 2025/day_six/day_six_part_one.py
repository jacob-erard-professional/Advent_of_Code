import numpy as np
arr = []
with open('day_six/day_six_data_one.txt') as f:
    for line in f:
        nums = list(map(int, line.split()))
        arr.append(nums)
arr = np.array(arr)
ops = []
with open('day_six/day_six_data_two.txt') as f:
    for line in f:
        ops = line.split()
        
count = 0
for i in range(len(arr[0])):
    if ops[i] == '+':
        count+= np.sum(arr[:, i])
    else:
        count += np.prod(arr[:, i])
print(count)