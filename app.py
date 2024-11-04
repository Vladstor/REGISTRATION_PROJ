from flask import Flask, render_template, redirect, request, url_for
from models import db, User
from flask_sqlalchemy import SQLAlchemy
from flask import session, abort
import os

app = Flask(__name__)

# Налаштування бази даних
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'  # Правильний ключ
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Вимкнення відстеження змін
#app.secret_key = os.urandom(24)

db.init_app(app)

@app.route('/register', methods=['GET', 'POST'])
def register(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Користувач з таким email вже існує"
        
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()  # Виправлено: правильне написання commit()

        #session['user_email'] = email

        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/success')
def success():
    if 'user_email' not in session:
        return redirect(url_for('register'))
    return render_template('success.html')  # Виправлена орфографія

#@app.route('/logout', methods=['POST'])
#def logout():
 #   if 'user_email' not in session:
  #      return abort(403)
   # session.pop('user_email', None)  # Видаляємо email з сесії
    #return redirect(url_for('register'))  # Повертаємо на сторінку реєстрації


if __name__ == '__main__': 
    app.run(debug=True)
