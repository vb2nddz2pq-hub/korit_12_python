import random

from ch05_hangman.hangman4 import stages
from ch05_hangman.hangman5 import words

word_list = words * 4

chosen_word = random.choice(word_list)


display = []
for _ in range(len(chosen_word)):
    display.append('_')

lives = 6
end_of_game = False

while not end_of_game:
    guess = input('알파벳을 입력하세요 >>> ').lower()

    # 이미 맞힌 글자인지 체크 (사용자 편의 기능)
    if guess in display:
        print(f"이미 입력해서 맞힌 글자 '{guess}'입니다.")
        continue

    # 단어 안의 글자 교체 작업
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # 오답 처리
    if guess not in chosen_word:
        lives -= 1
        print(f"틀렸습니다! '{guess}'는 단어에 없습니다.")
        print(f"(남은 기회: {lives})")

        if lives == 0:
            end_of_game = True
            print(f"아쉽네요! 정답은 '{chosen_word}'였습니다.")
            print(stages[0])  # 마지막 죽은 모습 출력
            break  # 게임 종료

    # 현재 상태 출력
    print(f"현재 진행상황: {' '.join(display)}")

    # 승리 조건 확인
    if "_" not in display:
        end_of_game = True
        print("🎉 정답입니다! 축하합니다!")

    # 현재 기회에 맞는 행맨 그림 출력
    if not end_of_game:
        print(stages[lives])