# Ввод трех целых чисел
A = int(input("Введите первое целое число A: "))
B = int(input("Введите второе целое число B: "))
C = int(input("Введите третье целое число C: "))

# Проверка истинности высказывания «Справедливо двойное»
is_double = (A == B) or (A == C) or (B == C)

# Вывод результата
if is_double:
    print("Справедливо двойное: True")
else:
    print("Справедливо двойное: False")