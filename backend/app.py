# Backend server for AISA project

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "AISA backend server is running"

@app.route("/status")
def status():
    return "AISA project is active and learning in progress"

@app.route("/issue", methods=["POST"])
def issue():
    data=request.json
    return data
