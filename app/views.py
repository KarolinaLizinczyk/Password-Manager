import base64
from flask import request, render_template
from flask_login import login_user, login_required
from app import app, db
from .models import PasswordManager, User
from .forms import PasswordManagerForm, UserForm


@app.route('/', methods=['GET', 'POST'])
def index():

    form = PasswordManagerForm(request.form)
    if request.method == 'POST':
        entry = PasswordManager(request.form['site_name'], request.form['site_url'], request.form['login_name'], request.form['password'])

        db.session.add(entry)
        db.session.commit()

    all_entries = [u.__dict__ for u in PasswordManager.query.all()]
    if all_entries > 0:
        return render_template('index.html', form=form, all_entries=all_entries)

    return render_template('index.html', form=form)


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = UserForm(request.form)

    if request.method == 'POST':
        login_name = request.form['login_name']
        password = request.form['password']
        user = User.query.filter_by(user_name=login_name).first()
        user_password = User.query.filter_by(_password=password).first()

        if not user:
            print('User not found')
        elif not user_password:
            print('Password is incorrect')
        login_user(user)
        return render_template('login.html', login_form=login_form)

    return render_template('login.html', login_form=login_form)

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    entry = PasswordManager.query.filter_by(id=id).first()
    form = PasswordManagerForm()

    form.site_name.data = entry.site_name
    form.site_url.data = entry.site_url
    form.login_name.data = entry.login_account_name
    decoded_pass = base64.b64decode(entry.password)
    form.password.data = decoded_pass

    if request.method == 'POST':
        PasswordManager.query.filter_by(id=id).update(
            dict(site_name=request.form['site_name'], site_url=request.form['site_url'],
                 login_name=request.form['login_account_name'], password=request.form['password']))
        db.session.commit()
        return render_template('edit.html', form=form, entry=entry, password=decoded_pass)
    return render_template('edit.html', form=form, entry=entry, password=decoded_pass)


@app.route('/delete/<id>', methods=['GET'])
def delete(id):
    PasswordManager.query.filter_by(id=id).delete()
    db.session.commit()
    all_entries = [u.__dict__ for u in PasswordManager.query.all()]
    if all_entries > 0:
        return render_template('index.html', all_entries=all_entries)
    return render_template('index.html')



