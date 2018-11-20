from app import db
import base64

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





