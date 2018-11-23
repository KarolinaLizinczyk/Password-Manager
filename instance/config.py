from binascii import hexlify
import os

SECRET_KEY = "OurCSRFSecretKey1390"

TEMPLATES_AUTO_RELOAD = True
##SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:test123@localhost/db_password'
##SQLALCHEMY_BINDS = {'user': 'postgresql://postgres:test123@localhost/db_password'}
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
TOKEN_SECRET = 'MySecretishSecret'

BCRYPT_LOG_ROUNDS = 12