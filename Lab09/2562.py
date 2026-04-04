li=[]
for i in range(9):
    li.append(int(input()))
maxval = max(li)
valid = li.index(maxval)+1
print(maxval)
print(valid)

