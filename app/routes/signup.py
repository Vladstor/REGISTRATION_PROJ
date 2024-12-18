from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models import User, db

bp = Blueprint('signup', __name__, url_prefix='/signup')

@bp.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        phone = request.form['phone']
        username = request.form['username']

        # Перевірка наявності користувача
        existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
        if existing_user:
            flash("Користувач з таким email або ім'ям вже існує.")
            return redirect(url_for('signup.signup'))
        
        # Перевірка телефону
        existing_user_phone = User.query.filter_by(phone=phone).first()
        if existing_user_phone:
            flash("Некоректний номер телефону.")
            return redirect(url_for('signup.signup'))

        # Додавання нового користувача
        user = User(email=email, phone=phone, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash("Реєстрація пройшла успішно! Увійдіть в акаунт.")
        return redirect(url_for('login.login'))
    return render_template('signup.html')
