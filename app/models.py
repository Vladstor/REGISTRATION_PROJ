import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, email, password, username, phone=None):
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.phone = phone
        self.username = username

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def create_table():
        """Create the users table if it doesn't exist."""
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='pswd1234',
            database='agro_reg_db'
        )
        with connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(45) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    phone VARCHAR(20),
                    username VARCHAR(45) NOT NULL
                )
            ''')
        connection.commit()
        connection.close()

    def save(self):
        """Insert a new user into the database."""
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='pswd1234',
            database='agro_reg_db'
        )
        with connection.cursor() as cursor:
            cursor.execute('''
                INSERT INTO users (email, password_hash, phone, username)
                VALUES (%s, %s, %s, %s)
            ''', (self.email, self.password_hash, self.phone, self.username))
        connection.commit()
        connection.close()

    @staticmethod
    def get_user_by_email(email):
        """Retrieve a user by email."""
        connection = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='pswd1234',
            database='agro_reg_db'
        )
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user_data = cursor.fetchone()
        connection.close()
        return user_data
