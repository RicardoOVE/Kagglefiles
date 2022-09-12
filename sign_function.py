def sign(number):
    if number > 0:
        return 1
    elif number == 0:
        return 0
    elif number < 0:
        return -1

print(sign(0.001))