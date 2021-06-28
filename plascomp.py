from flask import Flask
from flask.templating import render_template
from os import system

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

def mauve(plasmid):
    """
        Gets the plasmid fasta sequence and performs mauve aligment on them
        Returns an alignment:In-browser??
    """
    ref = plasmid[-1]
    to_compare = plasmid[:-1]

    #Housekeeping first
    if not plasmid or len(plasmid) == 1:
        return "Mauve should at least get two fasta files for comparison"
    numb = ''   # of sequences to align
    system(f'progressiveMauve --output={numb.xmfa} {plasmid}')

if __name__ == "__main__":
    app.run(debug=True)