import random
numbers = [1,2,3,4,5]
chosen_number = random.choice(numbers)
print(chosen_number)



# todo -1 : word_list에서 하나의 단어를 임의로 선택하도록 random 모튤을
# 사용하고, 해당 단어를 chosen_word 변수에 담으시오

# todo -2 : 사용자에게 알파벳 하난를 추측해서 입력하라고 요청하고,
# 이를 guess 변수에 담으시오 대문자로 싲가하는 경우 방지를.lower()를 적용하시오
# todo -3 : guess에서 입력한 문자 하나가 chosen_word의 str 문자열 중에
# 하나의 문자와 일치하는지를 확인할 수 있도록 반복-조건문을 작성하고
# 맞으면 정답 / 틀리면 오답이라고 출력하시오

'''
예를 들어 단어가 apple이고 p라고 입력했다면
오답
정답
정답
오답
'''
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
guess = input('알파벳 하나를 추측해보세요>>>').lower()

# 단어 안에 사용자가 입력한 알파벳이 포함되어 있는지 바로 확인
if guess in chosen_word:
    print("정답!")
else:
    print("오답!")



