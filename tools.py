"""Дві допоміжні функції, які main.py підключає через import tools."""


def is_even(n):
    return n % 2 == 0


def max3(a, b, c):
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m
