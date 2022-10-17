import csv

RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[107m'
BLACK = '\u001b[30m'
END = '\u001b[0m'
GRAY = '\u001b[00m'
GREEN = '\u001b[42m'

def flag_cz():
    for i in range(4):
        if i <= 1:
            print(f'{WHITE}{"  " * 10}{END}')
        else:
            print(f'{RED}{"  " * 10}{END}')

print(flag_cz())

def uzor():
    for i in range(5):
        if i == 0:
            print(f'{BLUE}{"                    "}{END}')
        if i == 1:
            print(f'{WHITE}{"     "}{BLUE}{" "}{WHITE}{"     "}{BLUE}{" "}{WHITE}{"     "}{BLUE}{" "}{WHITE}{"  "}{END}')
        if i == 2:
            print(f'{BLUE}{"                    "}{END}')
        if i == 3:
            print(f'{WHITE}{"  "}{BLUE}{" "}{WHITE}{"     "}{BLUE}{" "}{WHITE}{"     "}{BLUE}{" "}{WHITE}{"     "}{END}')
        if i == 4:
            print(f'{BLUE}{"                    "}{END}')
        if i == 5:
            print()
print(uzor())

def diagram(x, y):
    a = max(x, y)
    b = x + y - max(x, y)
    c = a - b
    for i in range(c):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ')
    for i in range(b):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ' + GREEN + 3 * ' ' + GRAY + 3 * ' ')
        print(GRAY + 3 * ' ' + str(a) + '%' + GRAY + 3 * ' ' + str(b) + '%' + GRAY + 3 * ' ')

def function():
    for i in range(9, 0, -1):
        if i == 1:
            print(i, RED + ' ' + WHITE + 9 * '   ')
        elif i == 2:
            print(i, WHITE + ' ' + RED +  '       ' + END)
        elif i == 3:
            print(i, WHITE + '        ' + RED + '         ' + END)
        elif i >3:
            print(i, WHITE + 19 * ' ' + END)
    print('0 1 2 3 4 5 6 7 8 9')

function()
print(' ')

def diagram(x, y):
    a = max(x, y)
    b = x + y - max(x, y)
    c = a - b
    for i in range(c):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ')
    for i in range(b):
        print(GRAY + 3 * ' ' + RED + 3 * ' ' + GRAY + 3 * ' ' + GREEN + 3 * ' ' + GRAY + 3 * ' ')
    print(GRAY + 3 * ' ' + str(a) + '%' + GRAY + 3 * ' ' + str(b) + '%' + GRAY + 3 * ' ')

with open ('books-utf8.csv', 'r', encoding='utf-8') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    count = 0
    count2017 = 0
    for row in table:
        if row[0] == 'ID':
            continue
        count += 1
        if row[6][6:11] <= "2017":
            count2017 += 1

bf2017 = int((count2017/count)*100)
af2017 = int(((count-count2017)/count)*100)

def diagram(n, m):
    print(GREEN + ' ' * n + END + '\n')
    print(RED + ' ' * m + END)
    print('        10        20        30        40        50        60        70        80        90        100')

print(diagram(bf2017, af2017))

