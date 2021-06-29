from flask import Flask
from flask.templating import render_template
from os import system
import urllib
from urllib import request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

def blast(plasmid):
    """
    Gets a plsmid seq & blasts it & returns a description summary of the results in csv format
    """
    blast_url = ''
    blasted = request.urlopen(blast_url)
    if blasted:
        navigate_to_ncbi(blast_url)
    return "There was an error with blast"

@app.route('/blastbone')
def navigate_to_ncbi(url):
    """Redirects to ncbi after click"""
    return render_template('blastbone.html',url=url)
if __name__ == "__main__":
    app.run(debug=True)