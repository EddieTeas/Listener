import sqlite3
import os


def create_database():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    sql_command = """
    CREATE TABLE users (
        name TEXT,
        username TEXT,
        password TEXT); """
    cursor.execute(sql_command)
    add_initial_user()


def add_initial_user():
    name = "Zanetta Tyler"
    username = "zrtyler"
    password = "1111"
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    sql_command = """
            INSERT INTO users(name, username, password)
            VALUES (?, ?, ?);
            """
    cursor.execute(sql_command, (name, username, password))
    connection.commit()

def add_initial_user():
    name = "Edward Teasley"
    username = "ewteasl1"
    password = "2222"
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    sql_command = """
            INSERT INTO users(name, username, password)
            VALUES (?, ?, ?);
            """
    cursor.execute(sql_command, (name, username, password))
    connection.commit()

def add_user(name, username, password):
    connection = sqlite3.connect("data/users.db")
    cursor = connection.cursor()
    sql_command = """
            INSERT INTO users(name, username, password)
            VALUES (?, ?, ?);
            """
    cursor.execute(sql_command, (name, username, password))
    connection.commit()


def login(username, password):
    connection = sqlite3.connect("data/users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? and password=?;", (username, password))
    result = cursor.fetchall()
    if result:
        for r in result:
            return r
    else:
        return None


def get_usernames():
    connection = sqlite3.connect("data/users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT username FROM users")
    print("fetchall:")
    result = cursor.fetchall()
    for r in result:
        print(r)


if __name__ == "__main__":
    create_database()
    login("zrtyler", "1111")
