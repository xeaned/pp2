import psycopg2

conn = psycopg2.connect(
    database="phonebook",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

conn.autocommit = True
cur = conn.cursor()

# Создание таблицы
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    phone_number VARCHAR(255)
)
""")

# Создание функции и процедур (один раз)
procedures_sql = """
-- 1. Поиск по паттерну
CREATE OR REPLACE FUNCTION search_by_pattern(pattern TEXT)
RETURNS TABLE (user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE username ILIKE '%' || pattern || '%' OR phone_number ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. Вставка или обновление
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_username TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = p_username) THEN
        UPDATE phonebook SET phone_number = p_phone WHERE username = p_username;
    ELSE
        INSERT INTO phonebook(username, phone_number) VALUES (p_username, p_phone);
    END IF;
END;
$$;

-- 3. Массовая вставка с проверкой
CREATE OR REPLACE PROCEDURE insert_many_users(data TEXT[][], OUT invalid_entries TEXT[][])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
BEGIN
    invalid_entries := ARRAY[]::TEXT[][];
    WHILE i <= array_length(data, 1) LOOP
        IF data[i][2] !~ '^\\d{11,15}$' THEN
            invalid_entries := invalid_entries || ARRAY[[data[i][1], data[i][2]]];
        ELSE
            CALL insert_or_update_user(data[i][1], data[i][2]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;

-- 4. Пагинация
CREATE OR REPLACE FUNCTION get_paginated_users(p_limit INT, p_offset INT)
RETURNS TABLE (user_id INT, username TEXT, phone_number TEXT) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook ORDER BY user_id LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

-- 5. Удаление
CREATE OR REPLACE PROCEDURE delete_user(p_username TEXT DEFAULT NULL, p_phone TEXT DEFAULT NULL)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook 
    WHERE (username = p_username AND p_username IS NOT NULL) 
       OR (phone_number = p_phone AND p_phone IS NOT NULL);
END;
$$;
"""

cur.execute(procedures_sql)

# === Python функции ===
def search_pattern():
    pattern = input("Enter pattern to search: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    for row in cur.fetchall():
        print(row)

def insert_or_update():
    name = input("Username: ")
    phone = input("Phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    print("User inserted or updated.")

def insert_many():
    users = []
    n = int(input("How many users? "))
    for _ in range(n):
        name = input("Username: ")
        phone = input("Phone: ")
        users.append([None, name, phone])

    cur.execute("CALL insert_many_users(%s)", (users,))
    cur.execute("SELECT * FROM phonebook")
    print("Current records:")
    for row in cur.fetchall():
        print(row)

def pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_paginated_users(%s, %s)", (limit, offset))
    for row in cur.fetchall():
        print(row)

def delete_user():
    name = input("Username (or leave blank): ") or None
    phone = input("Phone (or leave blank): ") or None
    cur.execute("CALL delete_user(%s, %s)", (name, phone))
    print("User deleted if found.")

def print_all():
    cur.execute("SELECT * FROM phonebook")
    for row in cur.fetchall():
        print(row)

def menu():
    while True:
        print("""
1 - Search by pattern
2 - Insert or update user
3 - Insert many users
4 - Get paginated users
5 - Delete user
6 - Print all
0 - Exit
""")
        choice = input("Choose option: ")
        if choice == '1':
            search_pattern()
        elif choice == '2':
            insert_or_update()
        elif choice == '3':
            insert_many()
        elif choice == '4':
            pagination()
        elif choice == '5':
            delete_user()
        elif choice == '6':
            print_all()
        elif choice == '0':
            break

menu()

cur.close()
conn.close()
