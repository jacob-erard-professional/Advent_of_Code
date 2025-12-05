fresh_items = []
with open('day_five/day_five_data.txt', 'r') as f:
    for line in (f):
        f, l = line.split('-')
        fresh_items.append(((int(f)), (int(l))))

stack = []
fresh_items.sort(key= lambda x: x[0])

count = 0
start = fresh_items[0][0]
end = fresh_items[0][1]
for range in fresh_items[1:]:
    if range[0] <= end:
        end = max(end, range[1])
    else:
        count+= end-start + 1
        start = range[0]
        end = range[1]
        
print(count + (end-start) + 1)