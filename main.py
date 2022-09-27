import pylab


def main():
    GetStop = 0

    while GetStop != 'stop' or 'Stop' or 'STOP':
        GetNumbers1 = float(input('Enter your number: '))
        GetOperation = input('Choose a operation (+, -, *, /): ')
        GetNumbers2 = float(input('Enter your number: '))

        if GetOperation == '+':
            print(GetNumbers1, GetOperation, GetNumbers2, '=', GetNumbers1 + GetNumbers2)
        elif GetOperation == '-':
            print(GetNumbers1, GetOperation, GetNumbers2, '=', GetNumbers1 - GetNumbers2)
        elif GetOperation == '*':
            print(GetNumbers1, GetOperation, GetNumbers2, '=', GetNumbers1 * GetNumbers2)
        elif GetOperation == '/':
            print(GetNumbers1, GetOperation, GetNumbers2, '=', GetNumbers1 / GetNumbers2)

        GetStop == 'stop' or 'Stop' or 'STOP'
        break




    return 0


main()
