def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b


def main():
    while True:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

        operation = input("Введите тип операции: ")

        if operation == '-':
            print(sub(a, b))
        elif operation == '+':
            print(add(a, b))
        elif operation == '*':
            print(mul(a, b))
        elif operation == '/':
            print(div(a, b))
        else:
            print("Завершена работа программы.")
            break

main()