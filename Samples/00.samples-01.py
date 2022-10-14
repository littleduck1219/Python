import random

random_number = random.randint(1,100)

game_count = 1

while True:
  try:

    my_number = int(input("1-100 사이 숫자를 입력하세요"))

    if my_number > random_number:
      print('Down!!')
    elif my_number < random_number:
      print('UP')
    else:
      print(f'축하합니다. {game_count} 만에 맞추셨습니다.')
      break

game_count = game_count + 1
