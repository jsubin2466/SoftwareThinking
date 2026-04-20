#8진수를 2진수로 전환
#2:의 이유는 앞에 0b가 붙기 때문
a = input()
print(bin(int(a, 8))[2:])
