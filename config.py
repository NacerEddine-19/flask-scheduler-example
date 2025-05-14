import os
basedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'databases')


class Config(object):
    # main config
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    BCRYPT_LOG_ROUNDS = 12

    # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SECURITY_PASSWORD_SALT = 'email-confirm-key'

    # mail accounts
    ADMINS = [os.environ.get('MAIL_USERNAME')]
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_USERNAME')


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
