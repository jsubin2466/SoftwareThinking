t = int(input())
for _ in range(t):
    n = input()
    count = 0

    for i in n:
        if i=='(':
            count += 1
        elif i==')':
            count += -1
        if count < 0:
            break

    if count == 0:
        print('YES')
    else:
        print('NO')
        
