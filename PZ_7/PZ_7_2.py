#Дана строка-предложение на русском языке. Зашифровать её, выполнив циклическую замену
#каждой буквы на следующюю за ней в алфавите и сохранив при этом регистр букв. Букву ё не
#учитывать. Знаки препинания и пробелы не изменять.
def encrypt_text(text):
    # Определяем русский алфавит без буквы ё
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    alphabet_upper = alphabet.upper()
    # Создаем словари для замены
    shift_dict = {char: alphabet[(index + 1) % len(alphabet)] for index, char in enumerate(alphabet)}
    shift_dict_upper = {char: alphabet_upper[(index + 1) % len(alphabet_upper)] for index, char in
                        enumerate(alphabet_upper)}
    encrypted_text = []
    for char in text:
        if char in shift_dict:
            encrypted_text.append(shift_dict[char])
        elif char in shift_dict_upper:
            encrypted_text.append(shift_dict_upper[char])
        else:
            encrypted_text.append(char)  # Знаки препинания и пробелы остаются без изменений
    return ''.join(encrypted_text)
# Пример использования
input_text = "Привет, мир! Как дела?"
encrypted = encrypt_text(input_text)
print(encrypted)