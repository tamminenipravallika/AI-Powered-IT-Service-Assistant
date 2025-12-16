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
    user_issue = data["issue"].lower()

    if "vpn" in user_issue or "network" in user_issue:
        category="Network issue"
        solution="Please check your internet connection and restart the VPN."
    elif "password" in user_issue or "signin" in user_issue or "login" in user_issue or "signup" in user_issue:
        category="Access issue"
        solution="Please try resetting your password or contact IT support."
    elif "laptop" in user_issue or "computer" in user_issue or "slow" in user_issue:
        category="Hardware issue"
        solution="Please restart your laptop and close unused applications."
    else:
        category="General IT issue"
        solution="Your issue has been noted. IT support will contact you."

return{
    "issue"=user_issue,
    "category"=category,
    "suggested_solution"=solution
}
   

