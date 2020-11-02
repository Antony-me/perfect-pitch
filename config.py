import os

class Config:

    SECRET_KEY = 'stuxnet993.'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/perfectpitch'

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



class ProdConfig(Config):
    # pass


    SQLALCHEMY_DATABASE_URI = 'postgres://zxdamayblnrtfv:0eeac4d61218e3145038337efaecc4137a23539271e1f16e9721aa0e780608a7@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d39q1rfdq4e4ch'


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}