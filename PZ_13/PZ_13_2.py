#Сгенерировать двумерный список, в которой элементы больше 10 заменяются на 0.

import random

# Генерация двумерного списка размером 5x5 с случайными числами от 0 до 20
rows, cols = 5, 5
matrix = [[random.randint(0, 20) for _ in range(cols)] for _ in range(rows)]

# Замена элементов больше 10 на 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > 10:
            matrix[i][j] = 0

# Вывод результата
print("Исходный двумерный список:")
for row in matrix:
    print(row)

print("\nОбновленный двумерный список:")
for row in matrix:
    print(row)
