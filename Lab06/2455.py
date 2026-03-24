people = 0
ll =[]

for i in range(4):
	a,b = map(int, input().split())
	people += b
	people -= a
	ll.append(people)

print(max(ll))

 
