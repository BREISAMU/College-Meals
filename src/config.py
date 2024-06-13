import os

class Config:

    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = '09864bd9d44a86672762c56e965dee334a8330fc'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'samueljbreider@gmail.com'

    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_PASSWORD = 'bijgtbfdmaanydbd'




