import time
import os

#Smazání konzole
clear = lambda : os.system('cls')

#Zastavení programu na x sekund
sleep = lambda x : time.sleep(x) 
rows = 7
cols = 10
cinema = []

#Vytvoření 2d pole
for y in range(rows):
    cinema.append([0 for x in range(cols)])

#Vypíše sál do konzole v hezké podobě
def print_cinema():
    print('* * * Plátno * * * *')
    for y in range(rows):
        for x in range(cols):
            print(cinema[y][x], end=" ")
        print()

#Zkontroluje dostupnost zadaného místa
def is_avaible(y, x):
    return True if cinema[y][x] == 0 else False

#Nastavení zadaného místa
def set_seat(y, x):
    if is_avaible(y,x):
        cinema[y][x] = 1
        return True
    return False

#Zkontroluje a nastaví pozice místa
def check_values(y,x):
    if y > 6 or y < 0 or x > 9 or x < 0:
        wrong = True
        while wrong:
            clear()
            print_cinema()
            print('Zadané hodnoty jsou velké/malé!')
            y = int(input('Zadejte řadu - (1-7): ')) - 1
            x = int(input('Zadejte sedadlo - (1-10): ')) - 1
            if not(y > 6 or y < 0 or x > 9 or x < 0):
                wrong = False
    return y, x           

#Hlavní smyčka
while True:
    clear()
    mode = int(input('Vyberete co chcete - rezervace míst(0), zobrazení sálu(1): '))
    if mode == 1:
        clear()
        print_cinema()
        back = int(input('Chcete zpět do menu? - Ano(1)/Ne(0): '))
        while back == 0:
            clear()
            print_cinema()
            back = int(input('Chcete zpět do menu? - Ano(1)/Ne(0): '))
    else:
        clear()
        print_cinema()
        y = int(input('Zadejte řadu - (1-7): ')) - 1
        x = int(input('Zadejte sedadlo - (1-10): ')) - 1
        y, x = check_values(y, x)
        if not(set_seat(y,x)):
            taken = True
            while taken:
                clear()
                print_cinema()
                print('Zadané míšsto je obsazené!')
                y = int(input('Zadejte řadu - (1-7): ')) - 1
                x = int(input('Zadejte sedadlo - (1-10): ')) - 1
                y, x = check_values(y, x)
                if set_seat(y,x):
                    clear()
                    taken = False
                    print('Místo zarezervováno!')
                    sleep(2)
        else:
            clear()
            print('Místo zarezervováno!')
            sleep(2)