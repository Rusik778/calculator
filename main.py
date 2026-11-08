from calc import add, sub, mul, div, power, percent
import tools


def main():
    while True:
        print("\n1 — додати; 2 — відняти; 3 — помножити; 4 — поділити")
        print("5 — піднести до степеня")
        print("6 — обчислити відсоток від числа")
        print("7 — перевірити парність; 8 — найбільше з трьох")
        print("0 — вихід")
        choice = input("Оберіть дію: ").strip()
        if choice == "0":
            print("Роботу завершено.")
            break
        if choice not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print("Невідома дія.")
            continue
        if choice == "7":
            try:
                n = int(input("Ціле число: "))
            except ValueError:
                print("Помилка: введіть ціле число.")
                continue
            print("Парне" if tools.is_even(n) else "Непарне")
            continue
        if choice == "8":
            try:
                a = float(input("a = "))
                b = float(input("b = "))
                c = float(input("c = "))
            except ValueError:
                print("Помилка: введіть число.")
                continue
            print("Результат:", tools.max3(a, b, c))
            continue
        try:
            a = float(input("Перше число: "))
            b = float(input("Друге число: "))
        except ValueError:
            print("Помилка: введіть число.")
            continue
        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = sub(a, b)
        elif choice == "3":
            result = mul(a, b)
        elif choice == "4":
            result = div(a, b)
        elif choice == "5":
            result = power(a, b)
        elif choice == "6":
            result = percent(a, b)
        if result is None:
            print("Дію не визначено: перевірте ділення на нуль або степінь.")
        else:
            print("Результат:", result)


if __name__ == "__main__":
    main()
