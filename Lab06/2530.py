a,b,c = map(int, input().split())
d = int(input())
sec = (c+d)%60
min = (b+(c+d)//60)%60
h = (a + (b+(c+d)//60)//60)%24
print(h, min, sec)
