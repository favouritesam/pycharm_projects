def numbers(num):
    for i in range(num):
        if (i % 3 == 0) and (i % 5 == 0):
            print("fizzBuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


numbers(100)
