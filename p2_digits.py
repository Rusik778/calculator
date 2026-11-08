"""Завдання П2 1.4, переписане у вигляді функції."""


def count_digits(n):
    if n < 0:
        raise ValueError("Число має бути невід’ємним")
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


if __name__ == "__main__":
    try:
        n = int(input("Невід’ємне ціле число: "))
        print("Цифр:", count_digits(n))
    except ValueError as error:
        print("Помилка:", error)
