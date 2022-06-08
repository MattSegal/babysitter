from flask import Flask, render_template, Response

from .camera import generateVideo
from .audio import generateAudio

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/video_feed")
def video_feed():
    return Response(
        generateVideo(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )


@app.route("/audio_feed")
def audio_feed():
    return Response(generateAudio(), mimetype="audio/x-wav;codec=pcm")
