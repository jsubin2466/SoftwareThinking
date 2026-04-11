def d(n):
    a=n//1000
    b=n//100%10
    c=n//10%10
    e=n%10
    return (n+a+b+c+e)
numli=[]
for i in range(1,10001):
    numli.append(d(i))
for j in range(1,10001):
    if j not in numli:
        print(j)
