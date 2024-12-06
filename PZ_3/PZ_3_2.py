def calculator():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    while True:
        choice = input("Введите номер операции (1/2/3/4) или 'q' для выхода: ")

        if choice == 'q':
            print("Выход из калькулятора.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))

                if choice == '1':
                    result = num1 + num2
                    operation = "+"
                elif choice == '2':
                    result = num1 - num2
                    operation = "-"
                elif choice == '3':
                    result = num1 * num2
                    operation = "*"
                elif choice == '4':
                    if num2 == 0:
                        print("Ошибка: Деление на ноль невозможно.")
                        continue
                    result = num1 / num2
                    operation = "/"

                print(f"{num1} {operation} {num2} = {result}")
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректные числа.")
        else:
            print("Ошибка: Неверный выбор операции.")

# Запуск калькулятора
calculator()
