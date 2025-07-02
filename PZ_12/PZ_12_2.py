#Составить генератор (yield), который переведет символы строки из верхнего
#регистра в нижний.
def to_lowercase_generator(input_string):
    for char in input_string:
        yield char.lower()

# Пример использования генератора
input_str = "Hello, World!"
lowercase_gen = to_lowercase_generator(input_str)

# Выводим символы в нижнем регистре
for lower_char in lowercase_gen:
    print(lower_char, end='')

# Если нужно получить всю строку в нижнем регистре
# можно использовать join
lowercase_string = ''.join(to_lowercase_generator(input_str))
print("\nСтрока в нижнем регистре:", lowercase_string)