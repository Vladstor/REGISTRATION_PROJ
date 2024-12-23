from app.routes.signup import bp as signup_bp
from app.routes.login import bp as login_bp
from app.routes.home import bp as home_bp

__all__ = ['signup_bp', 'login_bp', 'home_bp']