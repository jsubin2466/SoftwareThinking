alpb = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
inpt = input()
total = 0
for i in inpt:
	if i in alpb:
		total += alpb.index(i)+1
if total == 1:
	print("It is a prime word.")	
else:
	for k in range(2, int(total**(0.5)+1)):
		if total%k==0:
			print("It is not a prime word.")
			break
	else:
		print("It is a prime word.")	
