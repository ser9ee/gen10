from random import randint
from math import log, ceil
        
compNum = randint(1, 50)
num = 0
score = 50
att = ceil(log(50, 2)) - 1
flag = False
asterisk = '*' * 47
res = 'N'
lang = 'EN'

def game_ru(asterisk, att, num, compNum, flag, score):
    print(f'{asterisk}\nСгенерировано целое число от 1 до 50.\nУ Вас есть {att} попыток, чтобы его угадать.')
    print(f'{asterisk}\nВведите число: ', end='')
    while att > 0:
        num = input()
        try:
            num = int(num)
            print(asterisk)
            if num == compNum:
                att -= 1
                flag = True
                break
            elif num not in range(1, 51):
                print('\nВведенное число вне допустимого диапазона!\n\nПопробуйте снова: ', end='')
            else:
                att -= 1
                score -= 10            
                if att != 0:
                    print('\nОшибка! Загаданное число больше.\n' if num < compNum else '\nОшибка! Загаданное число меньше.\n')
                    print(f'Осталось попыток: {att}\nПопробуйте снова: ', end='')           
        except:
            print('\nВведено не целое число!\n\nПопробуйте снова: ', end='')
            continue
    if flag == True:
        print(f'\nОтличная работа!\n\nЗагаданное число: {num}\nНабрано очков: {score}\nИспользовано попыток: {5 - att}\n')
    else:
        print(f'Попыток больше не осталось :(\n\nЗагаданное число: {compNum}\nНабрано очков: {score}\n')
        
def game_en(asterisk, att, num, compNum, flag, score):
    print(f'{asterisk}\nThe program generates a number from 1 to 50.\nYou have {att} attempts to guess it.')
    print(f'{asterisk}\nTry to guess what number has been generated: ', end='')
    while att > 0:
        num = input()
        try:
            num = int(num)
            print(asterisk)
            if num == compNum:
                att -= 1
                flag = True
                break
            elif num not in range(1, 51):
                print('\nThe entered number is out of range!\n\nTry again: ', end='')
            else:
                att -= 1
                score -= 10            
                if att != 0:
                    print('\nWrong! The guessed number is greater.\n' if num < compNum else '\nWrong! The guessed number is less.\n')
                    print(f'Attempts left: {att}\nTry again: ', end='')           
        except:
            print('\nNot an integer entered!\n\nTry again: ', end='')
            continue
    if flag == True:
        print(f'\nGood job!\n\nThe target number is: {num}\nYour score is: {score}\nUsed attempts: {5 - att}\n')
    else:
        print(f'Sorry, you have no more attempts :(\n\nThe target number is: {compNum}\nYour score is: {score}\n')

def lang(lang):
    lang = input('Language / Язык (EN / RU): ')
    lang = lang.upper()
    if lang == 'RU':
        game_ru(asterisk, att, num, compNum, flag, score)
    else:
        game_en(asterisk, att, num, compNum, flag, score)
        
lang(lang)

while res != 'Y':
    res = input('Restart / Заново (Y / N): ')
    res = res.upper()
    if res == 'Y':
        compNum = randint(1, 50)
        num = 0
        score = 50
        att = 5
        flag = False
        asterisk = '*' * 47
        res = 'N'
        lang(lang)   
    else:
        break    
