from random import randint


compNum = randint(1, 10)
num = 0
score = 100
flag = True
tryAgain = 'Try again: '
aster = '*' * 32
print(aster)
print('Enter an integer from 1 to 10: ', end='')
while score > 0:
    num = input()
    try:
        num = int(num)
        print(aster)
        if num != compNum and 0 < num < 11:
            score -= 20
            if score != 0:
                print('Guessed wrong! ;)\n')
                print('Attempts left:', int(score / 20))
                print(tryAgain, end='')
                continue
            continue
        elif num == compNum:
            num = compNum
            flag = False
            break
        elif num > 10:
            print('The Number is too big!\n', tryAgain, sep='', end='')            
            continue
        elif num < 1:
            print('The Number is too small!\n', tryAgain, sep='', end='')            
            continue        
    except:
        print('Not an integer entered!\n', tryAgain, sep='', end='')
        continue
    
if flag == False:
    print('Victory!\n\nThe target Number is:', num, '\nYour score is:', score)
else: print('No more attempts left :(', '\nYour score is:', score)
print()
print(input('Push Enter to Quit'))