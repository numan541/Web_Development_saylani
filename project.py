from flask import Flask, render_template, request
import os
project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
print(project_dir)
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# db.create_all()

class User(db.Model):
    name = db.Column(db.String(40),unique=True, nullable=False, primary_key = True)
    password = db.Column(db.String(40),unique=False, nullable=False)
    city = db.Column(db.String(40),unique=False, nullable=False)
@app.route("/")
def hello():
    return render_template('index.html')
@app.route("/admin.html")
def admin():
    return render_template('admin.html')
@app.route("/portal.html")
def portal():
    return render_template('portal.html')
@app.route("/teacher.html")
def teacher():
    return render_template('teacher.html')

app.run(debug=True)
