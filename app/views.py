from app import app, db
from flask import request, render_template, flash

from .models import PasswordManager
from .forms import PasswordManagerForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PasswordManagerForm(request.form)
    if request.method == 'POST':
        entry = PasswordManager(request.form['site_name'], request.form['site_url'], request.form['login_name'], request.form['password'])
        print(entry)
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html', form=form)


