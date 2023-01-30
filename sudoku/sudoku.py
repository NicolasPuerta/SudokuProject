import random
import os 
import numpy
import time

def timerEjetator(i):
    if os.name == 'nt':
        os.system('cls')
        print( f'{int((i)/3600)}:{int(((i)/60)%60)}:{(i)%60}' )
        time.sleep(1)
    else:
        os.system('clear')
        print( f'{int((i)/3600)}:{int(((i)/60)%60)}:{(i)%60}' )
        time.sleep(1)


def timer(condition):
    i=0
    while condition:
        i+=1
        timerEjetator(i)

def DrawBoardBase():
    # BaseBoard = [[' ' for i in range(9)]]*9 # no FUNCIONA con esto INTENTAR ARREGLAR
    BaseBoard=[[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)]]
    for i in range(len(BaseBoard)):
        choicecolumn = random.choice([1,2,3,4])
        for j in range(choicecolumn):
            unknown = random.randint(0,9)
            rowelection = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            while FindSimilar(BaseBoard,unknown,i,rowelection) == True:
                unknown = random.randint(1,9)
            if unknown==0:
                BaseBoard[i][rowelection] = ' '
            else:
                BaseBoard[i][rowelection] = unknown
    return BaseBoard

def Draw(base):
    display = ''
    display += '|'+''.join(['-' for i in range(35)])+'|'+'\n'
    for i in range(len(base)):
        display += '| '
        for j in range(len(base[i])):
            display += str(base[i][j])+' | '
        display += '\n'
        display += '|'+''.join(['-' for i in range(35)])+'|'+'\n'
    print(display)

def FindSimilar(base,unknown,column,row):
    return unknown in base[column]
    y=[fila[row] for fila in base]
    return unknown in y
    return False

if __name__ == '__main__':
    timer(True)