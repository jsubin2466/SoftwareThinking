a = int(input())
cycle = 0
answ = a

while (1==1):
	b = answ//10
	c = answ%10
	d = (b+c)%10
	answ = 10*c + d

	cycle = cycle + 1
	if(answ == a):
		break

print(cycle)
