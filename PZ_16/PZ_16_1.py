#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.
class Book:
    def __init__(self, title, author, pages):
        self.title = title          # название книги
        self.author = author        # автор книги
        self.pages = pages          # количество страниц

    def read(self):
        return f'Чтение книги: "{self.title}" автор {self.author}, {self.pages} страниц.'

    def write(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        return f'Данные книги обновлены: "{self.title}" автор {self.author}, {self.pages} страниц.'

# Пример использования
book = Book("Война и мир", "Лев Толстой", 1225)
print(book.read())
print(book.write("Анна Каренина", "Лев Толстой", 864))
print(book.read())