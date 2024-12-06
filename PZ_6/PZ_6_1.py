def generate_list(N, A, B):
    # Проверяем, что N больше 2
    if N <= 2:
        raise ValueError("N должно быть больше 2")

    # Инициализируем список с первыми двумя элементами
    result = [A, B]

    # Заполняем оставшиеся элементы списка
    for i in range(2, 10):
        next_value = sum(result)  # Сумма всех предыдущих элементов
        result.append(next_value)  # Добавляем новый элемент в список

    return result


# Пример использования
N = 5  # любое значение больше 2
A = 3
B = 4

result_list = generate_list(N, A, B)
print("Сформированный список:", result_list)