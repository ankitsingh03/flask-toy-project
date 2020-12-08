from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '4d730385b427acb609897f7dd2e5b360'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# use for password coding and decording
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)


from flaskproperty import routes
