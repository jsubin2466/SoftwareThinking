n=int(input())
li=list(map(int, input().split()))
li.sort  #큰거에서 작은거 뺴야하므로 sort 처리

count = 0
ttt = 0

for i in range(n):
    count += li[i]*i-ttt #6 앞에 1,3 있으면 6-1+6-3=6*2-1-3인 것
    ttt += li[i] ###ttt에는 작은 값들이 순서대로 담김 

print(count*2)

