
class Config(object):
    SECRET_KEY = b'\x96\xdcA\xfc\xc9\x99\xd29\x84qY\x1bR\xdcUx'

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mayfarm.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_PATH = 'application/static'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
