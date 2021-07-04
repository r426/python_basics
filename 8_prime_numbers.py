# Implementation of the Sieve of Eratosthenes algorithm
# to find all prime numbers from 2 to the N
# (with the help of GeeksforGeeks)

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def primeNumbers(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p)


primeNumbers(number())