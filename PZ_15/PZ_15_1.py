#Приложение для туристического агентства ТУР. Таблица Турист должна
#содержать следующую информацию о клиентах турфирмы: Код клиента, Клиент
#(Фамилия), Телефон, Название страны, Регион, Продолжительность поездки,
#Стоимость путевки.'
import sqlite3
# Создание и подключение к базе данных
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn
# Создание таблицы "Турист"
def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Турист (
            Код_клиента INTEGER PRIMARY KEY AUTOINCREMENT,
            Фамилия TEXT NOT NULL,
            Телефон TEXT NOT NULL,
            Название_страны TEXT NOT NULL,
            Регион TEXT NOT NULL,
            Продолжительность_поездки INTEGER NOT NULL,
            Стоимость_путевки REAL NOT NULL
        )
    ''')
    conn.commit()
# Добавление нового туриста
def add_tourist(conn, фамилия, телефон, название_страны, регион, продолжительность_поездки, стоимость_путевки):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Турист (Фамилия, Телефон, Название_страны, Регион, Продолжительность_поездки, Стоимость_путевки)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (фамилия, телефон, название_страны, регион, продолжительность_поездки, стоимость_путевки))
    conn.commit()
# Отображение всех туристов
def display_tourists(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Турист')
    tourists = cursor.fetchall()
    for tourist in tourists:
        print(f'Код клиента: {tourist[0]}, Фамилия: {tourist[1]}, Телефон: {tourist[2]}, '
              f'Страна: {tourist[3]}, Регион: {tourist[4]}, '
              f'Продолжительность поездки: {tourist[5]} дней, '
              f'Стоимость путевки: {tourist[6]} руб.')
# Основная функция
def main():
    database = "tourism_agency.db"
    # Создание подключения к базе данных
    conn = create_connection(database)
    # Создание таблицы
    create_table(conn)
    # Добавление примеров туристов
    add_tourist(conn, 'Иванов', '123-456-7890', 'Испания', 'Коста-Брава', 7, 5000.00)
    add_tourist(conn, 'Петров', '987-654-3210', 'Италия', 'Тоскана', 10, 8000.00)
    # Отображение всех туристов
    print("Список туристов:")
    display_tourists(conn)
    # Закрытие подключения к базе данных
    conn.close()
if __name__ == '__main__':
    main()