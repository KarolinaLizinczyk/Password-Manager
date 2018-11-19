from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from app import db, bcrypt


class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site_name = db.Column(db.String(64), nullable=False)
    site_url = db.Column(db.String(128), nullable=False)
    login_account_name = db.Column(db.String(128), nullable=False)
    _password = db.Column(db.Binary(60))

    def __init__(self, site_name, site_url, login_account_name, plaintext_password):
        self.site_name = site_name
        self.site_url = site_url
        self.login_account_name = login_account_name
        self.password = plaintext_password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)




