list = {5, 8, 3, 3, 5, 2, 7, 1, 14}

for i in list:
    if i % 2 == 0:
        print(i)


def is_even(number):
    return number % 2 == 0


def fetch_even_numbers_from(numbers):
    result = []
    for number in numbers:
        if is_even(number):
            result.append(number)
        return result
