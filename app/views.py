from app import app
from flask import request, render_template, url_for, redirect, flash, session



@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')


