import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
guess = input('알파벳을 입력하세요 >>>').lower()
for i in range(word_length):
    display.append("_")
print(f'현재 상태:{' '.join(display)}')

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:
        display[i] = guess
        print(display)


