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
word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(f'test word : {chosen_word}')
display = []
for _ in range(len(chosen_word)):
    display.append('_')
lives = 6
end_of_game = False
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