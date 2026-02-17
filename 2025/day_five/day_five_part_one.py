fresh_items = set()
with open('day_five/day_five_data.txt', 'r') as f:
    for line in f:
        f, l = line.split('-')
        fresh_items.add((int(f), int(l)))
count=0         
with open('day_five/day_five_data_2.txt') as f:
    for lin in f:
        for rang in fresh_items:
            if int(lin) > rang[0] and int(lin) < rang[1]:
                count+=1
                break
print(count)