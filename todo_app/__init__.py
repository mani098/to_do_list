from flask import Flask
import os
from flask.ext.sqlalchemy import SQLAlchemy
from todo_app import views

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
app = Flask(__name__, template_folder=tmpl_dir, static_folder=static_dir)

views.LoginView.register(app, '/')
views.DashboardView.register(app, '/')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin2aphick:zRGVwhBHFEul@127.11.170.2/todo'
db = SQLAlchemy(app)
BaseModel = db.Model

app.config.from_pyfile('app.cfg')
db.init_app(app)


