from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10))  # Виправлення: db.String замість db.Varchar
    username = db.Column(db.String(30), nullable=False)  # Додано поле username
