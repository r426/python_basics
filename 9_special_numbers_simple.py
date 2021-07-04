# Find out if it is a special number:
# composed of only odd prime digits and
# the sum of its digits is an even number.

# Simple implementation.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def isSpecial(num):
    if num == 0:
        return False
    sum = 0
    while num > 0:
        digit = num % 10
        if digit == 3 or digit == 5 or digit == 7:
            sum += digit
            num //= 10
        else:
            return False
    if sum % 2 == 0:
        return True
    else:
        return False


print(isSpecial(number()))
