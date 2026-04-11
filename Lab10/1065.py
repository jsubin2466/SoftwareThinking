k = int(input())
def x(n):
    a=n//100
    b=n//10%10
    c=n%10
    if (a+c==2*b):
        return n
if k<100:
    print(k)
else:
    count = 99
    for _ in range(100, k+1):
        if x(_)==_:
            count+=1
    print(count)

