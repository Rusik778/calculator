"""Додаткове завдання: рекурсивна сума цифр."""


def digit_sum_rec(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + digit_sum_rec(n // 10)


if __name__ == "__main__":
    try:
        n = int(input("Ціле число: "))
        print("Сума цифр:", digit_sum_rec(n))
    except ValueError:
        print("Помилка: введіть ціле число.")
