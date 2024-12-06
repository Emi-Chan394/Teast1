def find_max_local_minimum(arr):
    if len(arr) < 3:
        raise ValueError("Список должен содержать как минимум 3 элемента для поиска локальных минимумов.")

    local_minima = []

    # Проходим по списку, начиная со второго элемента и заканчивая предпоследним
    for i in range(1, len(arr) - 1):
        if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            local_minima.append(arr[i])

    # Если локальные минимумы найдены, возвращаем максимальный из них
    if local_minima:
        return max(local_minima)
    else:
        return None  # Если локальных минимумов нет


# Пример использования
arr = [9, 6, 3, 8, 7, 5, 10, 4, 2]
max_local_min = find_max_local_minimum(arr)

if max_local_min is not None:
    print("Максимальный локальный минимум:", max_local_min)
else:
    print("Локальные минимумы не найдены.")