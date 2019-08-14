import os

<<<<<<< HEAD

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mannuh:123@localhost/maranara'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
=======
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smoucha:mumo@localhost/laundry'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True

>>>>>>> 46337212cf55e7be709f95ebbcee78780c204023
    @staticmethod
    def init_app(app):
        pass

<<<<<<< HEAD

class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mannuh:123@localhost/maranara'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

    

class TestConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mannuh:123@localhost/maranara_test'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mannuh:123@localhost/maranara'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
=======
class ProdConfig(Config):
    
    pass

class  DevConfig(Config):
    

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production':ProdConfig
}


>>>>>>> 46337212cf55e7be709f95ebbcee78780c204023
