# Assignment 1. Make a dictionary out of a list.

list1 = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dict = {}
for i in range(len(list1)):
    dict[i] = list1[0]
print(dict)

# Assignment 2. Guess a number.

import random

number = random.randrange(1,20)
for i in range(5):
    attempt = int(input('Введите число от 1 до 20:', ))
    if attempt > number:
        print('Слишком много!')
        if i == 4:
            print('Все, к сожалению, вы проиграли. Игра завершена.')
    elif attempt < number:
        print('Слишком мало!')
        if i == 4:
            print('Все, к сожалению, вы проиграли. Игра завершена.')
    else:
        print('Класс! Вы угадали!')
        break
         
            

# Assignment 3. A new string with three middle symbols from a given string.

odd_str = input('Введите строку длиой больше 7 символов: ', )
length = len(odd_str)
new_str = odd_str[length//2-1:length//2+2]
print(new_str)

# Assignment 4. Make one string out of two given strings.

#fem = str(input())
#male = str(input())
fem = 'Aidana'
male = 'Adilet'
new_str = ''
for i in range(len(male)):
    new_str += fem[i] + male[i]
print(new_str)

