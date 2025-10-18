def is_armstrong_number(number):
    str_number = str(number)
    length = len(str_number)
    total = 0
    for index in range(length):
        total += int(str_number[index])**length
    return total == number