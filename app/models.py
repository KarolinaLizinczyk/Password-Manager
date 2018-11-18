from sqlalchemy.ext.hybrid import hybrid_property
from app import db, bcrypt


class PasswordManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(64))
    site_url = db.Column(db.String(128))
    login_account_name = db.Column(db.String(128), unique=True)
    login_password = db.Column(db.String(128))

    def __repr__(self):
        return '<Site name {}>'.format(self.site_name)


    @hybrid_property
    def password(self):
        return self._password


    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)


