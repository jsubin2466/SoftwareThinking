n,k = map(int, input().split())
result=[]
for i in range(1, k+1):
	product = int(str(n*i)[::-1])
    result.append(product)
print(max(result))
