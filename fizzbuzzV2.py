def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return fizzbuzz
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


def print_fizzbuzz(n):
    for num in range(1, n+1):
        print(fizzbuzz(num))

print_fizzbuzz(300)

