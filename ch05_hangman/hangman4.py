import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
          r'''
            +---+
            |   |
            O   |
            |   |
                |
                |
          =========
          ''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요

# todo - 2 : while 문의 조건을 수정하여 6번의 기회가 소진되면 반복문이 종료 될 수 있도록 조건을 작성하시오
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(f'test word : {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display.append('_')

# todo - 1 : lives 변수를 while문 밖에서 선언
lives = 6
end_of_game = False

# todo - 2 : while문 안쪽의 들여쓰기를 확인하세요
while not end_of_game:
    guess = input('알파벳을 입력하세요 >>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"(남은 기회: {lives})")

        if lives == 0:
            end_of_game = True
            print(f"정답은 {chosen_word}였습니다.")


    print(f"현재 진행상황: {' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("정답!")
    print(stages[lives])