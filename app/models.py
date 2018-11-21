import base64
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from app import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(128), nullable=False)
    _password = db.Column(db.Binary(60))
    authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, user_name, plaintext_password):
        self.user_name = user_name
        self.password = plaintext_password

    def is_active(self):
        return True

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext).decode('utf-8')

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        if bcrypt.check_password_hash(self.password, plaintext_password):
            return True
        return False


class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site_name = db.Column(db.String(64), nullable=False)
    site_url = db.Column(db.String(128), nullable=False)
    login_account_name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(60))

    def __init__(self, site_name, site_url, login_account_name, password):
        self.site_name = site_name
        self.site_url = site_url
        self.login_account_name = login_account_name
        self.password = base64.b64encode(password)





