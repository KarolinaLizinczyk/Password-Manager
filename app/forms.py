from flask_wtf import Form
from wtforms import StringField, PasswordField, validators


class PasswordManagerForm(Form):
    site_name = StringField('Site Name', [validators.input_required(), validators.Length(min=5, max=35)])
    site_url = StringField('Site URL', [validators.input_required(), validators.Length(min=5, max=120)])
    login_name = StringField('Login Name', [validators.input_required(), validators.email(), validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.input_required()])

