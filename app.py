import glob
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    html_files = glob.glob("*.html")
    if not html_files:
        return "Aucun fichier HTML trouvé à la racine.", 404
    return send_file(html_files[0])
