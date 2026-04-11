def prime(n):
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return n
m = int(input())
n = int(input())
total = 0

for i in range(m,n+1):
    if prime(i)==i:
        total += i

if total==0:
    print('-1')
else: 
    print(total)
    
for _ in range(m, n+1):
    if prime(_)==_:
        print(_)
        break
