import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db

# Імпортуємо підмодулі для реєстрації, авторизації та головної сторінки
from app.routes.signup import bp as signup_bp
from app.routes.login import bp as login_bp
from app.routes.home import bp as home_bp

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='pswd1234'
)

def create_app():
    app = Flask(__name__)
    
    # Конфігурація додатка
    app.config.from_object('config.Config')
    

    # Ініціалізація бази даних
    db.init_app(app)

    create_database()
    
    # Реєстрація Blueprint для кожного модуля
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(home_bp)
    
    # Створення таблиць, якщо їх ще немає
    with app.app_context():
        db.create_all()

    return app


def create_database():
    global connection  # Ensure persistence of the connection
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS agro_reg_db")

    connection.database = 'agro_reg_db'
    cursor.close()