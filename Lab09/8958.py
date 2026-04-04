n = int(input())
li=[]
for _ in range(n):
    li.append(input())

for i in li:
    total = 0
    count = 0
    for j in i:
        if j == 'O':
            count += 1
            total += count
        else:
            count = 0
    print(total)

