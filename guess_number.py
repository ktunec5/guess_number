import random
secret_number = random.randint(1, 100)
tryes = 0
while True:
    question = input('Угадай число от 1 до 100: ')
    tryes += 1
    q = int(question)
    if q == secret_number:
        print(f'Да, верно! Это был номер {secret_number}! У тебя заняло {tryes} попыток.')
        break
    elif q > secret_number:
        print('Нет, не угадал! Чуть меньше!')
    elif q < secret_number:
        print('Нет, не угадал! Чуть больше!')


