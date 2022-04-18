import random

def main(attempt):
    game = True
    while game:
        count_attempt = 1
        computer = random.randint(1, 100)
        check_answer()
        new_game()

        
def new_game(user_unswer):
    while 1:
        print('Хотите сыграть еще раз? (Да/Нет)')
        if user_answer == 'нет':
            print('Вы вышли из игры')
            game = False
            break
        elif user_answer == 'да':
            break
        else:
            print('Kоманда не совсем понятна, повторите')


def left_attempt():
    print('У Вас осталось попыток:' + str(attempt - count_attempt))


def check_answer():
    game_round = True
    while game_round:
        user_number = input('Компьютер загадал число. Введите свое число! Чтобы получить подсказку дипазона чисел введите "?"')
        while not user_number.isnumeric() and not user_number == '?':
            print('Вы ввели букву или символ. Введите число!')
            user_number = input()
        if user_number == '?':
            print('Диапазон чисел от ' + str(computer - 10) + ' до ' + str(computer + 12) + ' У вас осталось попыток: ' + str(attempt+1 - count_attempt)) if computer > 10 else print('Диапазон чисел от ' + str(1) + ' до ' + str(computer + 10) + ' У вас осталось попыток: ' + str(attempt+1 - count_attempt))
            continue
        if user_number == str(computer):
            print('Вы угадали!')
            game_round = False
            break
        elif user_number > str(computer):
            print('Загаданое компьютером число меньше Вашего числа!')
            left_attempt()
        else:
            print('Загаданое компьютером число больше Вашего числа!')
            left_attempt()
        if count_attempt == attempt:
            print('Правильный ответ:' + str(computer))
            game_round = False
            break
        count_attempt += 1





main(3)