from flask_bootstrap import Bootstrap
from datetime import datetime
from operator import index
from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
import os
import urllib
from urllib import request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

# DB initializations
basedir = os.path.abspath(os.path.dirname(__file__))

# For querying mobBase

class QueryForm(FlaskForm):
    search = StringField('Enter the accession to search',validators=[DataRequired()])
    submit = SubmitField('Submit')

#App initializations

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir,'mobBase.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Databasing app
db = SQLAlchemy(app)

#Bootstraping 

bootstrap = Bootstrap(app)

#Model definition
class mobTable(db.Model):
    __tablename__ = "mobtable"

    sample_id = db.Column(db.String(64),primary_key=True)
    rep_type = db.Column(db.String(64),index=True)
    rep_type_accession = db.Column(db.String(64))
    predicted_mobility = db.Column(db.String(64),index=True)
    organism = db.Column(db.String(64),index=True)
    taxid = db.Column(db.String(64))

    def __repr__(self) -> str:
        return f'<Mob type for {self.organism} is {self.rep_type}>'

#App configurations for security reasons

app.config['SECRET_KEY'] = 'Credible bioinfor'

@app.shell_context_processor
def make_shell_context():
    return dict(db=db,mobTable=mobTable)


@app.route("/",methods = ['GET','POST'])
def home():
    form = QueryForm()
    q = ''
    #warning = ''
    if form.validate_on_submit():
        #global q
        q = mobTable.query.filter_by(sample_id=form.search.data).first()
        #if q is None:
            #warning = 'organism not found'
    
    #session['search'] = q
    form.search.data = ''
    return render_template('home.html',form=form,q = q)
if __name__ == "__main__":
    app.run(debug=True)