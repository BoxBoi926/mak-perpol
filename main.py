from flask import Flask, render_template, request
import csv
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)