#입력값: 현재 시간( 14 30 ) , 다음줄에 걸리는 시간 ( 20 ) 출력값( 14 50 ) 
hour, minute = map(int, input().split())
timer = int(input())

hour += timer//60
minute += timer%60
print(hour, minute)
