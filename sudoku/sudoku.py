import random
from os import system
import numpy
import time

def timer(condition):
    i=0
    while condition:
        system('cls')
        i+=1
        print( f'{int((i)/3600)}:{int(((i)/60)%60)}:{(i)%60}' )
        time.sleep(1)


if __name__ == '__main__':
    timer(True)