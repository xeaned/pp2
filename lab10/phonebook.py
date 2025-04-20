import psycopg2
import csv

conn = psycopg2.connect(
    database="phonebook", 
    user="postgres", 
    host='localhost',
    password="12345678", 
    port=5432
)

conn.autocommit = True

command_create_table = """
    CREATE TABLE IF NOT EXISTS phonebook ( 
        user_id SERIAL NOT NULL PRIMARY KEY, 
        username VARCHAR(255), 
        phone_number VARCHAR(255)
    )
"""
command_insert_into_csv = 'INSERT INTO phonebook (username, phone_number) VALUES (%s, %s)'
command_update_phone = 'UPDATE phonebook SET phone_number = %s WHERE user_id = %s'
command_update_name = 'UPDATE phonebook SET username = %s WHERE user_id = %s'
command_filter_name_starts = "SELECT * FROM phonebook WHERE username LIKE %s"
command_filter_phone_starts = "SELECT * FROM phonebook WHERE phone_number LIKE %s"
command_delete_by_phone = "DELETE FROM phonebook WHERE phone_number = %s"
command_delete_by_name = "DELETE FROM phonebook WHERE username = %s"

cur = conn.cursor()

# Функция для проверки существования таблицы
def check_table_exists():
    cur.execute("""
        SELECT EXISTS (
            SELECT FROM information_schema.tables 
            WHERE table_name = 'phonebook'
        );
    """)
    exists = cur.fetchone()[0]
    if not exists:
        print("Table does not exist, creating it...")
        cur.execute(command_create_table)
        print("Table created successfully.")
    else:
        print("Table already exists.")

# Функция для вставки данных из CSV
def csv_to_db(csv_file):
    with open(csv_file, 'r') as file_csv:
        reader_csv = csv.reader(file_csv, delimiter=',')
        for row in reader_csv:
            cur.execute(command_insert_into_csv, (row[0], row[1]))

# Функция для печати всех записей
def print_rows():
    cur.execute('SELECT * FROM phonebook')
    results = cur.fetchall()
    for row in results:
        print(row)

# Функция для добавления новой записи
def insert_to_db():
    username = input('Enter the username: ')
    phone = input('Enter the phone number: ')
    cur.execute(command_insert_into_csv, (username, phone))

# Функция для изменения имени
def change_name():
    new_username = input("Enter the new username: ")
    id = int(input('Enter the ID you want to change: '))
    cur.execute(command_update_name, (new_username, id))
    print_rows()

# Функция для изменения номера телефона
def change_phone_number():
    new_phone = input("Enter the new phone number: ")
    id = int(input('Enter the ID you want to change: '))
    cur.execute(command_update_phone, (new_phone, id))
    print_rows()

# Функция для фильтрации по имени
def filter_name_start_by():
    starts_with = input("Enter the letters that have to start with: ")
    cur.execute(command_filter_name_starts, (starts_with + '%',))
    results = cur.fetchall()
    for row in results:
        print(row)

# Функция для фильтрации по номеру телефона
def filter_phone_start_by():
    starts_with = input('Enter the digits that the phone number has to start with: ')
    cur.execute(command_filter_phone_starts, (starts_with + '%',))
    results = cur.fetchall()
    for row in results:
        print(row)

# Функция для удаления записи по номеру телефона
def delete_by_phone():
    phone_number = input('Enter the phone you want to delete: ')
    cur.execute(command_delete_by_phone, (phone_number,))
    print_rows()

# Функция для удаления записи по имени
def delete_by_name():
    name = input('Enter the name you want to delete: ')
    cur.execute(command_delete_by_name, (name,))
    print_rows()

# Функция для получения пользователей, чьи имена начинаются с заданной буквы
def get_starting_with(letter):
    command = 'SELECT username FROM phonebook WHERE LEFT(username, 1) = %s'
    try:
        cur.execute(command, (letter,))
        result = cur.fetchall()
        print(result)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

# Основная функция для получения команд от пользователя
def get_user_input():
    commands = """insert - Inserting into the database
change name - Changing the name of the user by the id
change phone number - Changing the phone number of the user by the id
filter by name - Filtering by the name that starts with the given value
filter by phone number - Filtering by the phone number that starts with the given value
delete by name - Deleting record by the name 
delete by phone number - Deleting record by the phone number
print all - Printing all records in the table
insert csv - Inserting all records to the database from the csv file
start with letter - Selecting usernames starting with the given letter"""
    print(commands)
    user_input = input("Enter the command: ")
    if user_input == 'insert':
        insert_to_db()
    elif user_input == 'change name':
        change_name()
    elif user_input == 'change phone number':
        change_phone_number()
    elif user_input == 'filter by name':
        filter_name_start_by()
    elif user_input == 'filter by phone number':
        filter_phone_start_by()
    elif user_input == 'delete by name':
        delete_by_name()
    elif user_input == 'delete by phone number':
        delete_by_phone()
    elif user_input == 'print all':
        print_rows()
    elif user_input == 'insert csv':
        csv_to_db('/Users/rapiyatleukhan/Desktop/pp2/lab10/phones.csv')
        print_rows()
    elif user_input == 'start with letter':
        letter = input('Enter the letter: ')
        get_starting_with(letter)

# Проверяем существование таблицы
check_table_exists()

# Получаем команду от пользователя
get_user_input()

# Закрываем соединение
cur.close()
conn.commit()
