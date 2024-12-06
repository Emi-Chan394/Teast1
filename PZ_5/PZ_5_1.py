def print_string_with_length(length):
    # Проверяем, что длина больше 0
    if length <= 0:
        print("Длина должна быть положительным числом.")
        return

    # Запрашиваем строку у пользователя
    user_input = input("Введите строку: ")

    # Проверяем, достаточно ли введенная строка длинной
    if len(user_input) < length:
        print(f"Введенная строка слишком короткая. Она содержит только {len(user_input)} символов.")
    else:
        # Выводим строку нужной длины
        output_string = user_input[:length]
        print(f"Выводим строку длиной {length}: '{output_string}'")


# Вводим длину строки с клавиатуры
try:
    desired_length = int(input("Введите количество символов для вывода: "))
    print_string_with_length(desired_length)
except ValueError:
    print("Пожалуйста, введите целое число.")
