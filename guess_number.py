from random import randint
number = random.randint(1, 100)
tryes = 0
print('Угадайте число от 1 до 100')
while True:
    question = int(input('Введите число: '))
    tryes += 1
    if question == number:
        print(f'Да, верно! Это был номер {number}! У тебя заняло {tryes} попыток.')
        break
    elif question > number:
        print('Нет, не угадал! Чуть меньше!')
    elif question < number:
        print('Нет, не угадал! Чуть больше!')


