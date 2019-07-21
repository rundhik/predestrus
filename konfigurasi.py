import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = '\xd7w;odC+\xb4\xc8\xd6~\x8ag\xee;!\x01\xd9\xb6c\xe5u\xfe\xe1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(apl):
        pass

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xd7w;odC+\xb4\xc8\xd6~\x8ag\xee;!\x01\xd9\xb6c\xe5u\xfe\xe1'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'estrus.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xd9J\xb23\xd2\x04\xd3N\xedYb\xbe\xe9\x1a\xd0\xc2\xf2G;M\xa8\xe0\xa8\x1e'