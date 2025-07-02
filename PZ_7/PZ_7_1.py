#Ден символ С, изображающий цифру или букву (латинскую или русскую). Если С изображает цифру,
#то вывести строку "digit", если латинскую букву - вывести строку "lat", если русскую букву -
#вывести строку "rus".
def identify_character(c):
    if c.isdigit():
        return "digit"
    elif c.isalpha():
        if 'а' <= c <= 'я' or 'А' <= c <= 'Я':
            return "rus"
        elif ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            return "lat"
    return "unknown"

# Пример использования
character = input("Введите символ: ")
result = identify_character(character)
print(result)