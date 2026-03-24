for i in range(3):
	a = list(map(int, input().split()))
	if a.count(1)==4:
		print("E")
	if a.count(1)==3:
		print("A")
	if a.count(1)==2:
		print("B")
	if a.count(1)==1:
		print("C")
	if a.count(1)==0:
		print("D")
