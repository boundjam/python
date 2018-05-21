def createListofFactors(num):
    print("TODO: Don't bug me. I am busy")
    return [1,2,3]


def askforNumbers():
    num1=int(input('give me a number:'))
    num2=int(input('give me another number:'))
    return num1, num2


if __name__ == '__main__':
    number1, number2 = askforNumbers()
    print(number1, number2)
    number1factors = createListofFactors(number1)
    print(number1factors)
    number2factors = createListofFactors(number1)
    print(number2factors)
