def recurse1(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + recurse1(n - 1)


def recurse2(n):
    if n == 0:
        return 1
    else:
        print(n)
        return n * recurse2(n - 1)


def sum(a, d, n):
    print(a, d, n)
    if n == 0:
        return 0
    return a + sum(a + d, d, n - 1)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def print_digits(num):
    if num < 10:
        print(num)
    else:
        print_digits(num // 10)
        print(num % 10)


def countup(n):
    if (n == 0):
        return []
    else:
        countArray = countup(n - 1)
        countArray.append(n)
        return countArray


print(recurse1(6))
print(recurse2(6))
print(factorial(5))
print(sum(2, 3, 4))
print_digits(9865)
print(countup(5))
