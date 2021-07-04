# Write a program using sys.argv that would depict the
# -	name of the script
# -	the number of the arguments and lastly the
# -	list of the arguments used.


import sys

lst = sys.argv
print('''Name of the script: {0}
Number of arguments: {1}
Arguments: {2}'''.format(lst[0], len(lst), lst))