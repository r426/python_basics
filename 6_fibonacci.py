# find out if N is a Fibonacci number
import math


def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def isSquare(n):
    if math.sqrt(n) - math.floor(math.sqrt(n)) == 0:
        return True
    else:
        return False


def isFibonacci(n):
    if isSquare(5 * n ** 2 + 4) or isSquare(5 * n ** 2 - 4):
        return True
    else:
        return False


print(isFibonacci(number()))
