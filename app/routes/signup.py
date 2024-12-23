from flask import Blueprint, request, jsonify, flash
import logging
from app.models import User

bp = Blueprint('signup', __name__, url_prefix='/signup')

@bp.route('/', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')
        username = data.get('username')

        if not email or not password or not phone or not username:
            return jsonify({'error': 'All fields are required'}), 400
        
        existing_user = User.get_user_by_email(email)
        if existing_user:
            return jsonify({'error': "User with this email or username already exists."}), 400

        new_user = User(email=email, password=password, phone=phone, username=username)
        new_user.save()

        return jsonify({'message': "Registration successful! Please log in."}), 201

    except Exception as e:
        logging.error(f"Error occurred during registration: {e}")
        return jsonify({'error': f'An error occurred. Please try again later. {str(e)}'}), 500
