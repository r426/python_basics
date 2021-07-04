# Generate the reverse of a given number N.

def number():
    while True:
        userInput = input('Please enter a big non-negative integer number: ')
        if userInput.isnumeric():
            return int(userInput)
        else:
            print("Input error.")


def reverse(number):
    reverseNumber = 0
    while number != 0:
        reverseNumber = reverseNumber * 10 + number % 10
        number //= 10
    return reverseNumber


print(reverse(number()))
