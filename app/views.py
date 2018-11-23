import base64
from flask import request, render_template, url_for, redirect
from flask_login import login_user, login_required
from app import app, db, login_manager
from .models import PasswordManager, User
from .forms import PasswordManagerForm, UserForm
import jwt
import datetime


# loginManager
@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()


@app.route('/', methods=['GET', 'POST'])
def index():
    login_form = UserForm(request.form)
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user = User.query.filter_by(user_name=user_name).first()
        print(user)
        if user.is_correct_password(password):
            login_user(user)
            return redirect(url_for('logged_in'))
        else:
            return redirect(url_for('index'))
    return render_template('index.html', login_form=login_form)


# Login
@app.route('/logged_in', methods=['GET', 'POST'])
@login_required
def logged_in():
    form = PasswordManagerForm(request.form)
    if request.method == 'POST':
        entry = PasswordManager(request.form['site_name'], request.form['site_url'], request.form['login_name'],
                                request.form['password'])
        db.session.add(entry)
        db.session.commit()
    all_entries = [u.__dict__ for u in PasswordManager.query.all()]
    if all_entries:
        return render_template('logged_in.html', form=form, all_entries=all_entries)
    return render_template('logged_in.html', form=form)


@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    entry = PasswordManager.query.filter_by(id=id).first()
    form = PasswordManagerForm()
    decoded_pass = base64.b64decode(entry.password + '='*(-len(entry.password) % 4))
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
        return render_template('logged_in.html', all_entries=all_entries)
    return render_template('logged_in.html')

@app.route('/issuetoken/<id>', methods=['GET'])
@login_required
def issuetoken(id):
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'resource': id
    }
    token = jwt.encode(payload, app.config['TOKEN_SECRET'], algorithm='HS256')
    tokenized_url = request.host_url + 'tokenized/' + token
    return tokenized_url

@app.route('/tokenized/<token>', methods=['GET'])
def tokenized(token):
    try:
        decoded = jwt.decode(token, app.config['TOKEN_SECRET'], algorithm='HS256')
    except jwt.ExpiredSignatureError:
        return 'Your token has expired'
    entryid = decoded['resource']
    entry = PasswordManager.query.filter_by(id=entryid).first()
    decoded_pass = base64.b64decode(entry.password + '='*(-len(entry.password) % 4))
    return render_template('entry.html', entry=entry, password=decoded_pass)
