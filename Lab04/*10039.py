#5명의 점수를 받는데 40미만은 40점으로 바꿈. 그리고 마지막에 평균 구하기
total = 0
for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    total += score
average = int(total//5)
print(average)
    
    

