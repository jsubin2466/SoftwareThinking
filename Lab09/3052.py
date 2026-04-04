li=[]
for _ in range(10):
    li.append(int(input()))
for i in range(len(li)):
    li[i] = li[i]%42
li_set=set(li)
print(len(li_set))
