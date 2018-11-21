import base64
from flask import request, render_template, url_for, redirect
from flask_login import login_user, login_required
from app import app, db, login_manager
from .models import PasswordManager, User
from .forms import PasswordManagerForm, UserForm


@app.route('/', methods=['GET', 'POST'])
@login_required
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


# loginManager
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = UserForm(request.form)

    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user = User.query.filter_by(user_name=user_name).first()
        print(user)
        if user.is_correct_password(password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html', login_form=login_form)


@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
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
                 login_account_name=request.form['login_name'], password=base64.b64encode(request.form['password'])))
        db.session.commit()
        return render_template('edit.html', form=form, entry=entry, password=decoded_pass)
    return render_template('edit.html', form=form, entry=entry, password=decoded_pass)


@app.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    PasswordManager.query.filter_by(id=id).delete()
    db.session.commit()
    all_entries = [u.__dict__ for u in PasswordManager.query.all()]
    if all_entries > 0:
        return render_template('index.html', all_entries=all_entries)
    return render_template('index.html')



