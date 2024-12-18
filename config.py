import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pswd1234@localhost/agro_reg_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #db = SQLAlchemy(app)