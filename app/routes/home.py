from flask import Blueprint

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return "<h1>Welcome to the Home Page!</h1><p>Ця сторінка буде оформлена пізніше.</p>"
