import io
import tests
import math
from matplotlib import pyplot as plt
import numpy as np
import random
import time

def fileread(data):
    with io.open(data,'r', encoding='utf-8') as file:
        file_data=file.read()
    numbers = list(map(int,file_data.split(' ')))
    return numbers
    print(numbers)
def main():
    global numbers
    print('Введите путь к файлу:')
    data= input()
    numbers=fileread(data)

    print('Min:', mini(numbers))
    print('Max:', maxi(numbers))
    print('Summa:', summa(numbers))
    print('Multiple:', multi(numbers))
    print('Результат теста:')
    genplt(9)
def _min(numbers):
    min_chislo=numbers[0]
    for i in numbers:
        min_chislo= min(min_chislo,i)
    return (min_chislo)

def _max(numbers):
    max_chislo = numbers[0]
    for i in numbers:
        max_chislo = max(max_chislo, i)
    return (max_chislo)

def _sum(numbers):
    summa=0
    for i in numbers:
        summa+=int(i)
    return(summa)

def _mult(numbers):
    mult=1
    for i in numbers:
        mult *= int(i)
    return mult
def genplt(kolvo_iter):
    n=1
    x=[]
    y=[]
    for j in range(kolvo_iter):
        numbers=[]
        for i in range(n):
            numbers.append(random.randint(-10**5,10**5))
            n*=5
        x.append(n)
        start_time=time.time()
        multi(numbers)
        end_time=time.time()
        y.append(end_time-start_time)
    plt.show()

main()
