from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from os import system
import urllib
from urllib import request

app = Flask(__name__)

# Databasing app
db = SQLAlchemy(app)

class mobTable(db.Model):
    __tablename__ = "mobtable"

    acession = db.Column(db.Integer,primary_key=True)

@app.route("/")
def home():
    pass

if __name__ == "__main__":
    app.run(debug=True)