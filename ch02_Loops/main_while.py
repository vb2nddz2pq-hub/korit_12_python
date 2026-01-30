'''
1 while 반복문
    while 다음에 나오는 조건식이 참이라면 이하이ㅢ 실행문이 반복 실행됨(조건식이 false가될때까지)
    형식 :
    while 조건식1:
    반복실행문1

    당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해주셔야 합니다
    중첩while문 당연히 가능

    기본 예제
    1부터 10까지 출력하기
'''
from calendar import firstweekday

n = 10
while n >= 1:
    print(n)
    n -= 1        # python에는 ++가 없습니다



for n2 in range(2, 10):
    for n3 in range(1,10):
        print(f"{n2} X  {n3} = {n2 * n3}")


