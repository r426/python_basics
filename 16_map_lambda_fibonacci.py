# Generate a list of the first N Fibonacci numbers.
# Then, apply the map function and a lambda expression
# to square each Fibonacci number and print the list.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def fibonacci(n):
    lst = [0]
    if n == 0: return lst
    lst.append(1)
    if n == 1: return lst
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst


fiboList = fibonacci(number())

fiboSquared = list(map(lambda n: n * n, fiboList))

print(fiboList)
print(fiboSquared)
