# Find out if it is a special number:
# composed of only odd prime digits and
# the sum of its digits is an even number.

# Implementation using a set.
# Challenge and algorithm by Avichal.

def number():
    while True:
        userInput = input('Please enter a non-negative integer number: ')
        if userInput.isnumeric():
            return userInput
        else:
            print("Input error.")


def isSpecial(num):
    if len(num) % 2 != 0:
        return False
    else:
        setNum = set(num)
        for x in setNum:
            if x != '3' and x != '5' and x != '7':
                return False
    return True


print(isSpecial(number()))
