import pymysql

class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name       = name
        self.gender     = gender
        self.dob        = dob
        self.location   = location

    def __str__(self):
        return f'Name:{self.name}, Location:{self.location}'

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='home_db', charset='utf8')
            print('DB connected')
            return connection
        except pymysql.MySQLError as e:
            print(f"DB connection failed: {e}")
            return None

    def disconnect_db(self, connection):
        try:
            if connection:
                connection.close()
                print('DB disconnected')
        except Exception as e:
            print(f"Error while disconnecting DB: {e}")

    def create_db(self):
        connection = self.connect_db()
        if connection:
            query = 'CREATE DATABASE IF NOT EXISTS nithin_db;'
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            print('DB created')
            self.disconnect_db(connection)

    def create_table(self):
        connection = self.connect_db()
        if connection:
            query = """
            CREATE TABLE IF NOT EXISTS persons(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(32) NOT NULL,
                gender CHAR CHECK(gender IN ('m', 'M', 'f', 'F')),
                location VARCHAR(32),
                dob DATE
            );
            """
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.close()
            print('Table created')
            self.disconnect_db(connection)

    def read_person_details(self):
        name = input('Enter person name: ')
        gender = input('Enter person gender: ')[0]
        location = input('Enter person location: ')
        dob = input('Enter person date of birth (yyyy-mm-dd): ')
        return (name, gender, location, dob)

    def insert_row(self, person):
        query = 'INSERT INTO persons(name, gender, location, dob) VALUES(%s, %s, %s, %s);'
        person_tuple = (person.name, person.gender, person.location, person.dob)
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, person_tuple)
            connection.commit()
            cursor.close()
            id = self.get_latest_row_id()
            self.disconnect_db(connection)
            return id
        return None

    def update_row(self, data):
        query = 'UPDATE persons SET name = %s, gender = %s, location = %s, dob = %s WHERE id = %s'
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)

    def delete_row(self, id):
        query = f'DELETE FROM persons WHERE id = {id}'
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'Person with id = {id} not found')
            else:
                print(f'Person with id = {id} deleted')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)

    def search_row(self, id):
        query = f'SELECT * FROM persons WHERE id = {id}'
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print(f'Person with id = {id} not found')
            else:
                row = cursor.fetchone()
                print(f'Person details are: {row}')
            connection.commit()
            cursor.close()
            self.disconnect_db(connection)
            return row
        return None

    def list_all_rows(self):
        query = 'SELECT * FROM persons;'
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            count = cursor.execute(query)
            if count == 0:
                print('No rows found in the table')
            else:
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            cursor.close()
            self.disconnect_db(connection)
            return rows
        return None

    def get_latest_row_id(self):
        query = 'SELECT MAX(id) FROM persons;'
        connection = self.connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute(query)
            id = cursor.fetchone()
            cursor.close()
            self.disconnect_db(connection)
            return id[0]
        return None

oprs = Db_operations()
latest_id = oprs.get_latest_row_id()
print(f"Latest ID: {latest_id}")