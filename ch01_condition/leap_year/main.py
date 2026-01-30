year = int(input('계산하고 싶은 년도를 입력하세요 >>>'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('윤년')
else:
    print('평년')
