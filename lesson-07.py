#"""
#SQL- Standart Query Language
#-DDL- Data definition Language
#	(CREATE TABLE )
#-DML- Data Manipulation Language
#	(SELECT, INSERT, UPDATE.DELETE)

# СУБД - Система управления базами данных
# Primary Key - (Первычеый ключ) Уникальныйй индентификаторе
# Может быть int, может быть str, может быть составной
# Foreign Key (внешний ключ)

#Алгоритм работы с БД:
#1. Установка соединения -- .connect()
#2. Создание обьекта курсора -- .cursor()
#3. Выполнение SQL- запроса(-ов) -- .execute()
#4. Если запрос изменяем данные/структуру 
#	4.1 зафиксировать изменения cursor.commit
#4. Если запрос на выборк (получение) данных
#	4.1 разобрать данные (fetch)
#"""


# SQLite3

import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('user.sqlite')
cursor = conn.cursor()

sql = """
CREATE TABLE  IF NOT EXISTS user(
	id  INTEGER PRIMARY KEY AUTOINCREMENT,
	firsthame TEXT NOT NULL,
	lastname TEXT NOT NULL,
	created DATETIME NOT NULL DEFAULY CURRENT_TIMESTAMP
	)
"""
cursor.execute(sql)
cinn.connect()

sql = """
INSERT INTO user(
	firsthame, lastname
	) VALUES (
		?, ?
	)
"""

cursor.execute(sql, ('Вася', 'Пупкин'))
conn.commit()

sql = """
	SELECT 
	id, firsthame, lastname, created
	FROM
	user
"""
cursor.execute(sql)
users = cursor.fetchall()
print(users)

conn.close()

#Используя контекстный менеджер все можно сократить

with sql.connect('users.sqlite') as conn:
	cursor = conn.execute(sql)
	users = cursor.fetchall
	print(users)