#!/usr/bin/python3

def num_test(str):
    
    '''
    Функция, проверяющая правильность ввода
    '''

    while True:
        try:
            x = float(input("Введите " + str + " значение: "))
            return x
        except ValueError:
            print("Вы ввели неправильный символ")
        else:
            break


if __name__ == "__main__":
    print("Для завершения программы введите q вместо знака операции ")
    while True:
        s = input("Введите знак операции (+, -, *, /)")
        if s == "q":
            print("Программа завершена")
            break
        elif s in ("+", "-", "*", "/"):
    # Ввод значений

            a = num_test("первое")
            b = num_test("второе")

    # Логика калькулятора и вывод ответа

            if s == '+':
                print('{} + {} = '.format(a, b), (a+b))
            elif s == '-':
                print('{} - {} = '.format(a, b), (a-b))
            elif s == '*':
                print('{} * {} = '.format(a, b), (a*b))
            elif s == '/':
                if b == 0:
                    print('{} / {} '.format(a, b))
                    print("Деление на ноль\nОперация невозможна")
                else:
                    print('{} / {} = '.format(a, b), (a/b))
        else:
            print("Неверный знак")