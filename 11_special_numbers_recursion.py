# Find out if it is a special number:
# composed of only odd prime digits and
# the sum of its digits is an even number.

# Implemented with recursion.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def add_digits(num):
    if num == 0:
        return 0
    else:
        digit = num % 10
        if digit == 3 or digit == 5 or digit == 7:
            return digit + add_digits(num // 10)
        else:
            print(False)
            exit()


n = number()

if n != 0 and add_digits(n) % 2 == 0:
    print(True)
else:
    print(False)
