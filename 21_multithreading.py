from threading import *


def displayEvenNumbers():
    i = 1
    print(current_thread().getName())
    while i <= 100:
        if i % 2 == 0:
            print(i)
        i += 1


def displayOddNumbers():
    i = 1
    print(current_thread().getName())
    while i <= 100:
        if i % 2 != 0:
            print(i)
        i += 1


t1 = Thread(target=displayEvenNumbers)
t1.start()

t2 = Thread(target=displayOddNumbers)
t2.start()

i = 1
print(current_thread().getName())
while i <= 100:
    print(i)
    i += 1
