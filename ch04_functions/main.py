'''
1 . 함수의 종류
 1) 파이썬 내장함수
 2) 메서드(methods)
 3) 사용자 정의 함수
2. 함수 용어 정리
 1) 함수 정의 : 사용자 정의 함수를 새로 만드는 것을 의미 (def : define)
 2) 인수(argument) : 함수에 전달할 입력값(input)
 3) 매개변수(parameter) : argument를 받아서 저장하는 변수를 의미
 4) 변환값/결과값/return값 : 함수의 출력값(output)
 5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미
3. (사용자 정의) 함수의 형식:
 1_함수 정의 부분
def 함수_이름(매개변수1,매개변수2):
    실행문
    return 뭐어쩌고

    2 함수 호출 부분
   변수 = 함수_이름(argument1,argument2)
'''

# eng_name = input('당신의 이름을 영어로 입력하세요 >>>')
# eng_name_low = eng_name.lower()
# eng_name_up = eng_name.upper()
# print(f'{eng_name_low} / {eng_name_up}')

'''
str 자료형에 딸려있는 .메서드명() 으로 호출하는 애들이 메서드입니다
.lower() str 데어트를 전부 소문자로 바꿔주고
.uppwer() str 데이터의 문자들을 전부 대문자로 바꿔주네요
특정 클래스에 종속되어있는 함수들을 method 라고 합니다
함수는 독립적으로 사용이 가능합니다

java / js 떄와 마찬가지로 call1() ~ call4() 유형으로 정의할 수 있습니다
'''
# def multiply(n):
#     print(f"구구단 {n}단 출력")
#     for i in range(1, 10):
#         print(f"{n} x {i} = {n * i}")
# dan = int(input("몇단을 출력하시겠습니까 >>> "))
# multiply(dan)

'''
연산자 중에 또 파이썬에만 있는거 소개
+
=
*
/
%
**
// : 몫 연산자 
'''
# print(5%2)
# print(5//2)

money = 3000
drink_count = 0
price = 700

while money >= price:
    print(f'음료수 ={drink_count}개, 잔돈={money}원')

    money -= price
    drink_count += 1
    if money < price:
        print(f'{drink_count}개,잔돈 ={money}원')
        break
        vending_machine(3000)



