from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_script import Manager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

login_manager = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

bcrypt = Bcrypt(app)
CSRFProtect(app)


from app import views, models, forms