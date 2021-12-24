import random as r

_number = []
bulls, cows = 0, 0

def start_print():
    print(
        'Правила: \n',
        ' Компьютер загадывает четырехзначное число, все цифры которого различны\n',
        'первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.\n',
        'Игрок вводит четырехзначное число c неповторяющимися цифрами,\n',
        'компьютер сообщают о количестве «быков» и «коров» в названном числе\n',
        '«бык» — цифра есть в записи задуманного числа и стоит в той же позиции,\n',
        'что и в задуманном числе\n',
        '«корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,\n',
        'что и в задуманном числе\n',
        'Например, если задумано число 3275 и названо число 1234,\n',
        'получаем в названном числе одного «быка» и одну «корову».\n',
        'Очевидно, что число отгадано в том случае, если имеем 4 «быка».\n\n'

    )


def get_number():
    result = []
    random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    num = random_list[r.random(1, 8)]
    random_list.remove(num)
    result.append(num)

    num = random_list[r.random(0, 8)]
    random_list.remove(num)
    result.append(num)

    num = random_list[r.random(0, 8)]
    random_list.remove(num)
    result.append(num)

    num = random_list[r.random(0, 8)]
    random_list.remove(num)
    result.append(num)

    global _number
    _number = result
def check_number(num):
        user_list = [int(x) for x in num]
        bulls = 0
        cows = 0
        for i in range(4):
            if user_list[i] == _number[i]:
                bulls += 1
            elif user_list[i] in _number:
                cows += 1
        result = {'быки - ': bulls, 'коровы - ': cows}
        return result

def game_over(num):
    user_input = [int(x) for x in num]
    if user_input == _number:
        return True
    else:
        return False