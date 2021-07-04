'''  1
    ##
   333
  ####
 55555   '''

try:
    userInput = float(input("Enter a number between 1 and 10: "))
    assert userInput.is_integer() and 1 <= userInput <= 10, "Invalid number."
except AssertionError as object:
    print(object)
else:
    intNumber = int(userInput)
    spaces = intNumber
    for row in range(intNumber):
        spaces -= 1
        for column in range(spaces): print(" ", end="")
        for column in range(intNumber - spaces):
            if (row + 1) % 2 == 1:
                print(row + 1, end="")
            else:
                print("#", end="")
        print("")
