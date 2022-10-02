# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр


def f(x):
    suma = 0
    for digit in n:
        if digit.isdigit():
            suma += int(digit)
    return print(suma)


n = input('Введите вещественное число' '\n') 
f(n)