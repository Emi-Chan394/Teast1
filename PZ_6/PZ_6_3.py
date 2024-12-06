def shift_right_and_replace_with_zero(arr, K):
    N = len(arr)

    if N <= K or K < 1:
        raise ValueError("Убедитесь, что 1 < K < N.")

    # Сдвигаем элементы вправо на K позиций
    for i in range(N - 1, K - 1, -1):
        arr[i] = arr[i - K]

    # Заменяем первые K элементов на 0
    for i in range(K):
        arr[i] = 0

    return arr


# Пример использования
arr = [1, 2, 3, 4, 5, 6]
K = 2
result = shift_right_and_replace_with_zero(arr, K)
print("Результат:", result)