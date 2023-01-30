import random
import os 
import numpy as np
import time
import asyncio
import datetime

def play():
    ini = datetime.datetime.now()
    boardbase = DrawBoardBase()
    bordpermanent = boardbase[0]
    bordplayed = boardbase[1]
    Draw(bordplayed)
    while True:
        modify = str(input("digita las cordenadas y el numero de esta forma columna-fila-numero: "))
        modify = modify.split('-')
        for i in range(len(modify)):
            modify[i]=int(modify[i]) 
        bordplayed = ModifyBoard(bordplayed,modify,bordpermanent)
        try:
            os.system('cls')
        except:
            os.system('clear')
        Draw(bordplayed)
        if bordpermanent[0][0] != bordplayed[0][0]:
            t = timer(ini)
            print(t)
            print(ini)
            break

def timerEjetator(i):
    # if os.name == 'nt':
    #     os.system('cls')
    #     time.sleep(1)
    # else:
    #     os.system('clear')
    #     time.sleep(1)
    return f'{int((i)/3600)}:{int(((i)/60)%60)}:{(i)%60}'


def timer(ini):
    fin = datetime.timedelta(seconds=datetime.datetime.now().second)
    calc = ini + fin
    return calc  


def DrawBoardBase():
    # BaseBoard = [[' ' for i in range(9)]]*9 # no FUNCIONA con esto INTENTAR ARREGLAR
    BaseBoard=[[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)],[" " for i in range(9)]]
    for i in range(len(BaseBoard)):
        choicecolumn = random.choice(range(1,4))
        for j in range(choicecolumn):
            unknown = random.randint(0,9)
            rowelection = random.choice(range(9))
            while FindSimilar(BaseBoard,unknown,i,rowelection) == True:
                unknown = random.randint(1,9)
            if unknown==0:
                BaseBoard[i][rowelection] = ' '
            else:
                BaseBoard[i][rowelection] = unknown
    npBorad = np.array(BaseBoard)
    return [npBorad,BaseBoard]

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
    if unknown in base[column]: return True
    y=[fila[row] for fila in base]
    if unknown in y : return True
    return False

def ModifyBoard(base,lista,basepermanent):
    if FindSimilar(base,int(lista[2]),int(lista[0]),int(lista[1]))==True or basepermanent[lista[0]][lista[1]]!=' ':
        return base
    elif FindSimilar(base,int(lista[2]),int(lista[0]),int(lista[1]))==False and basepermanent[lista[0]][lista[1]]==' ' and (lista[2]<=9 and lista[2]>=1):
        base[lista[0]][lista[1]]=lista[2]
        return base
    return base

if __name__ == '__main__':
    timer(True)