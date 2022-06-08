from flask import Flask, render_template, Response

from .camera import generateVideo

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generateVideo(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )
