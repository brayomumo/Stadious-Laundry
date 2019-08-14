import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smoucha:mumo@localhost/laundry'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    
    pass

class  DevConfig(Config):
    

    DEBUG = True

config_options = {
    'development': DevConfig,
    'production':ProdConfig
}


