from flask import Blueprint, request, flash, session, jsonify
from app.models import User
from werkzeug.security import check_password_hash  
import logging

bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route('/', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValueError("Email і пароль обов'язкові")

        user_data = User.get_user_by_email(email)
        if not user_data:
            raise ValueError("Користувача не знайдено")

        logging.debug(f"user_data: {user_data}")

        if check_password_hash(user_data['password_hash'], password):
            session['user_id'] = user_data['id']
            flash("Авторизація пройшла успішно!", "success")
            return jsonify({'message': "Успішний вхід!"}), 201
        else:
            return jsonify({"error": "Невірний email або пароль. Спробуйте ще раз."}), 400

    except Exception as e:
        logging.error(f"Сталася помилка при вході: {str(e)}")
        return jsonify({'error': f'Сталася помилка. Будь ласка, спробуйте пізніше. {str(e)}'}), 500
