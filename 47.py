def askforNumber(message):
    num = int(input(message))
    return num


if __name__ == '__main__':
    number1 = askforNumber("Give me the first number: ")
    number2 = askforNumber("Give me the second number: ")
    print(number1, number2)
