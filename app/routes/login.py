from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from app.models import User

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            flash("Авторизація пройшла успішно!", "success")
            return redirect(url_for('home.index'))
        else:
            flash("Невірний email або пароль. Спробуйте ще раз.", "danger")
    return render_template('login.html')
