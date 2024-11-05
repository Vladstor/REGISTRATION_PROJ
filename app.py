from flask import Flask, render_template, redirect, request, url_for
from models import db, User
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Налаштування бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        username = request.form['username']

        # Перевірка наявності користувачів
        existing_user_email = User.query.filter_by(email=email).first()
        existing_user_phone = User.query.filter_by(phone=phone).first()
        existing_user_username = User.query.filter_by(username=username).first()

        if existing_user_email:
            return "Користувач з таким email вже існує", 400
        if existing_user_phone:
            return "Користувач з таким номером телефону вже існує", 400
        if existing_user_username:
            return "Користувач з таким нікнеймом вже існує", 400

        # Додавання нового користувача
        user = User(email=email, password=password, phone=phone, username=username)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('success'))
    
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')  

# Тимчасова головна сторінка для майбутньої прив'язки
@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page!</h1><p>Ця сторінка буде оформлена пізніше.</p>"

if __name__ == '__main__': 
    app.run(debug=True)
