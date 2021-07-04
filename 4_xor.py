# There is an even number of all elements but one in the list
# Find which element repeats an odd number of times
# Requirements: O(1) space complexity; O(n) time complexity.

# Implemented with xor operator

myList = [0, 1, 5, 7, 7, 3, 2, 1, 5, 3, 4, 3, 0, 1, 5, 3, 2, 1, 4]

i = 0
found = -1

while found < 0:
    j = i + 1
    for k in range(j, len(myList)):
        if myList[i] == myList[k]:
            myList[k] ^= myList[j]
            myList[j] ^= myList[k]
            myList[k] ^= myList[j]
            j += 1
    if (j - i) % 2 == 1:
        found = myList[i]
    else:
        i = j
print(f'There is an odd number of {found}s.')

# Yet it was as simple as that (mentor's solution):

xored = 0
for x in myList: xored ^= x
print(f'There is an odd number of {xored}s.')
