#Даны температуры за месяц март. Необходимо найти количество положительных и отрицательных значений
#температур в месяце, самую низкую и самую высокую температуры, а также среднемесячное значение температуры.

# Данные: температуры за март (пример)
temperatures = [3, -1, 4, 2, -5, 0, 6, 7, -3, 5, -2, 1, 8, -4]

# Функция для анализа температур
def analyze_temperatures(temps):
    positive_count = sum(1 for temp in temps if temp > 0)
    negative_count = sum(1 for temp in temps if temp < 0)
    min_temp = min(temps)
    max_temp = max(temps)
    average_temp = sum(temps) / len(temps)

    return positive_count, negative_count, min_temp, max_temp, average_temp

# Вызов функции и получение результатов
positive_count, negative_count, min_temp, max_temp, average_temp = analyze_temperatures(temperatures)

# Вывод результатов
print(f"Количество положительных температур: {positive_count}")
print(f"Количество отрицательных температур: {negative_count}")
print(f"Минимальная температура: {min_temp}")
print(f"Максимальная температура: {max_temp}")
print(f"Среднемесячная температура: {average_temp:.2f}")