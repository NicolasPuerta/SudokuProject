import random
import os 
import numpy as np
import time
from  BD.schemas.schemas import user_schema,users_schema
from BD.user import db_client

def play():
    ini = time.perf_counter()
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
        if not NkowIfEnd(bordplayed):
            End(ini)
        break

def NkowIfEnd(base):
    for i in range(len(base)):
        for j in range(len(base[i])):   
            if FindSimilar(base,'',i,j):
                return True
    return False



def End(ini):
    try:
        os.system('cls')
    except:
        os.system('clear')
    t = timer(ini)
    name = input('digite nombre')
    record = CreateUser(name=name,timep=t)
    print( AddRecord(record) )
    time.sleep(5)
    try:
        os.system('cls')
    except:
        os.system('clear')
    print(DrawRecord(BestFive()))

def timerEjecutator(i):
    # if os.name == 'nt':
    #     os.system('cls')
    #     time.sleep(1)
    # else:
    #     os.system('clear')
    #     time.sleep(1)
    return f'{int((i)/3600)}:{int(((i)/60)%60)}:{(i)%60}'


def timer(ini):
    fin = time.perf_counter()
    calc = fin-ini
    return timerEjecutator(calc)


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

def CreateUser(name,timep):
    dict1 = {
        'fullname' : name,
        'time' : timep
    }
    return dict1

def AddRecord( user ):
    user_dict =dict(user)
    id = db_client.local.record.insert_one(user_dict).inserted_id
    new_user = user_schema(db_client.local.record.find_one({"_id":id}))
    return f'{new_user["fullname"]} tu tiempo es: {new_user["time"]}'

def BestFive():
    u = users_schema(db_client.local.record.find({}))
    u.sort(key=lambda e: e['time'])
    del u[5:]
    for i in range(len(u)):
        u[i].pop('id')
    return u

def DrawRecord(lista):
    po = [['-', '-', '-', '-', '-','-', '-', '-', '-', '-','-', '-', '-', '-', '-','-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-', '-'],
          ['S', 'C', 'O', 'R', 'E'],
          ['-', '-', '-', '-', '-','-', '-', '-', '-', '-','-', '-', '-', '-', '-','-', '-', '-', '-', '-', '-', '-','-', '-', '-', '-', '-']]
    display = ''
    for i in range(len(po)):
        for j in po[i]:
            display+=j
        display+='\n'
    for i in lista:
        display += f'{i["fullname"]}: {i["time"]}'
        display+='\n'
    display += '---------------------------'
    return display

if __name__ == '__main__':
    timer(True)

