#a내린사람 b탄사람
#내리고 탄 후의 그때 사람 수를 ll 리스트에 저장

people = 0
ll =[]

for i in range(4):
	a,b = map(int, input().split())
	people += b
	people -= a
	ll.append(people)

print(max(ll))

 
