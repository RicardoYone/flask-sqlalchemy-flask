from routes import alumno_router
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.before_first_request
def crear_db():
    db.create_all(app=app)


@app.route("/")
def index():
    return "El servidor funciona XDDDD"
