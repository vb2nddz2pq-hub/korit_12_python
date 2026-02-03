import random
import hangman_arts
import hangman_word_list
from ch05_hangman.hangman5 import chosen_word

print(hangman_arts.logo)

chosen_word = random.choice(hangman_word_list.word_list)
print(f'테스트 단어 : {chosen_word}')