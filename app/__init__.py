import pymysql
from flask import Flask
from app.models import User

# Імпортуємо підмодулі для реєстрації, авторизації та головної сторінки
from app.routes.signup import bp as signup_bp
from app.routes.login import bp as login_bp
from app.routes.home import bp as home_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    create_database()
    User.create_table()

    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)

    return app

def create_database():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='pswd1234'
    )
    with connection.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS agro_reg_db")
    connection.close()
