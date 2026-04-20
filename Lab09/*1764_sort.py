#중복된 값 찾는 알고리즘
n, m = map(int, input().split())
heard = set()
see = set()

for _ in range(n): 
    heard.add(input())
for _ in range(m):
    see.add(input())

result = sorted(heard and see)

print(len(result))
for i in result:
    print(i)



