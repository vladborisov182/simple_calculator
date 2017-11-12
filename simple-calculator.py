#Функция, проверяющая правильность ввода
def num_test(str):
    while True:
        try:
            x = float(input("Введите " + str + " значение: "))
            return x
        except ValueError:
            print("Вы ввели неправильный символ")
            continue
        break
#Калькулятор
print("Для завершения программы введите q вместо знака операции ")
while True:
    s = input("Введите знак операции (+, -, *, /)")
    if s is "q":
        print("Программа завершена")
        break
    if s in ("+", "-", "*", "/"):
# Ввод значений
        a = num_test("первое")
        b = num_test("второе")
# Логика калькулятора и вывод ответа
        if s == '+':
            print('{} + {} = '.format(a, b), (a+b))
        if s == '-':
            print('{} - {} = '.format(a, b), (a-b))
        if s == '*':
            print('{} * {} = '.format(a, b), (a*b))
        if s == '/':
            if b == 0:
                print('{} / {} '.format(a, b))
                print("Деление на ноль\nОперация невозможна")
            else:
                print('{} / {} = '.format(a, b), (a/b))
    else:
        print("Неверный знак")
