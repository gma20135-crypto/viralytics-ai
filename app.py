from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("viralytics-ai-v3-youtube-direct.html")
