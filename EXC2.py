# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def f(x):
    a = []
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        a.append(factorial)
        i += 1  
    return print(a)


n = int(input("введи число" '\n'))
f(n)