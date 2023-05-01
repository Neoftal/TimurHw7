import sqlite3

# Создаем соединение с базой данных
conn = sqlite3.connect('my_database.db')

# Создаем курсор для работы с базой данных
cursor = conn.cursor()

# Создаем таблицу countries
cursor.execute('''CREATE TABLE IF NOT EXISTS countries
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL)''')

# Добавляем записи в таблицу countries
cursor.execute("INSERT INTO countries (title) VALUES ('Россия')")
cursor.execute("INSERT INTO countries (title) VALUES ('США')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

# Создаем таблицу cities
cursor.execute('''CREATE TABLE IF NOT EXISTS cities
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   area REAL DEFAULT 0,
                   country_id INTEGER NOT NULL,
                   FOREIGN KEY(country_id) REFERENCES countries(id))''')

# Добавляем записи в таблицу cities
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Москва', 1)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Нью-Йорк', 2)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Шанхай', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Пекин', 3)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Токио', 4)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Париж', 5)")
cursor.execute("INSERT INTO cities (title, country_id) VALUES ('Берлин', 6)")

# Создаем таблицу employees
cursor.execute('''CREATE TABLE IF NOT EXISTS employees
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   city_id INTEGER NOT NULL,
                   FOREIGN KEY(city_id) REFERENCES cities(id))''')

# Добавляем записи в таблицу employees
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Иван', 'Иванов', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Петр', 'Петров', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Анна', 'Иванова', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ирина', 'Петрова', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Константин', 'Константинопольский', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Сергей', 'Сергеев', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ольга', 'Ольгинская', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Алексей', 'Алексеев', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Елена', 'Еленова', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Артур', 'Артуров', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Мария', 'Маринина', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Дмитрий', 'Дмитриев', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Наталья', 'Натальева', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Александр', 'Александров', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Екатерина', 'Екатеринова', 5)")

# Сохраняем изменения
conn.commit()

# Получаем список городов из базы данных
cursor.execute("SELECT id, title FROM cities")
cities = cursor.fetchall()

# Выводим список городов пользователю
print("Список городов:")
for city in cities:
    print(str(city[0]) + " - " + city[1])

# Получаем id города от пользователя
city_id = int(input("Введите id города для вывода списка сотрудников или 0 для выхода: "))

# Пока пользователь не введет 0, продолжаем работу программы
while city_id != 0:
    # Получаем информацию о сотрудниках из выбранного города
    cursor.execute('''SELECT employees.first_name, employees.last_name, countries.title, cities.title
                          FROM employees
                          JOIN cities ON employees.city_id = cities.id
                          JOIN countries ON cities.country_id = countries.id
                          WHERE cities.id = ?''', (city_id,))
    employees = cursor.fetchall()

    # Выводим информацию о сотрудниках
    print("Сотрудники в городе:")
    for employee in employees:
        print(employee[0] + " " + employee[1] + " - " + employee[2] + ", " + employee[3])

    # Получаем id города от пользователя
    city_id = int(input("Введите id города для вывода списка сотрудников или 0 для выхода: "))

# Закрываем соединение с базой данных
conn.close()
