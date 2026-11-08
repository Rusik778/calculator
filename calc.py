"""Арифметичні функції калькулятора."""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return None
    return a / b


def power(x, n=2):
    """Дійсний степінь; None для недопустимої операції."""
    if x == 0 and n < 0:
        return None
    if x < 0 and n != int(n):
        return None
    try:
        return x ** n
    except OverflowError:
        return None


def percent(value, rate):
    """Повертає rate відсотків від value: 15% від 200 дорівнює 30."""
    return value * rate / 100
