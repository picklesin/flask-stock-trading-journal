import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'yoursecretkey')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # mail server info
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'your@serveremail.com')
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'your@email.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', 'yourpassword')     # Use your generated App Password
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'your@serveremail.com')
  

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    MAIL_SUPRESS_SEND = True
  
