from flask import Flask, render_template, redirect, request, url_for, session, flash
from models import db, User
from werkzeug.security import check_password_hash
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

# Налаштування бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

db.init_app(app)

@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        username = request.form['username']

        # Перевірка наявності користувачів
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash("Користувач з таким email або ім'ям вже існує")
            return redirect(url_for('signup'))
        
        existing_user_phone = User.query.filter_by(phone=phone).first()
        if existing_user_phone:
            return "Некоректний номер телефону", 400

        
        
        

        # Додавання нового користувача
        user = User(email=email, phone=phone, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Реєстрація пройшла успішно, увійдіть в акаунт")
        return redirect(url_for('login'))
    
    
    #return render_template('signup.html')

# Авторизація користувача
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Перевірка наявності користувача
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            # Збереження інформації про авторизованого користувача в сесії
            session['user_id'] = user.id
            flash("Авторизація пройшла успішно!", "success")
            return redirect(url_for('home'))
        else:
            flash("Невірний email або пароль. Спробуйте ще раз.", "danger")
    return render_template('login.html')

@app.route('/success')
def success():
    return render_template('success.html')  

# Тимчасова головна сторінка для майбутньої прив'язки
@app.route('/home')
def home():
    return "<h1>Welcome to the Home Page!</h1><p>Ця сторінка буде оформлена пізніше.</p>"

if __name__ == '__main__': 
    app.run(debug=True)
