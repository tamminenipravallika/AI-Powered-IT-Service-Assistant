# Backend server for AISA project

from flask import Flask, request

app = Flask(__name__)
ticket_id = 1

@app.route("/")
def home():
    return "AISA backend server is running"

@app.route("/status")
def status():
    return "AISA project is active and learning in progress"

def classify_intent(user_issue):
     if "vpn" in user_issue or "network" in user_issue:
       return "Network issue"
    elif "password" in user_issue or "signin" in user_issue or "login" in user_issue or "signup" in user_issue:
        return "Access issue"
    elif "laptop" in user_issue or "computer" in user_issue or "slow" in user_issue:
        return "Hardware issue"
    else:
        "General IT issue"

@app.route("/issue", methods=["POST"])
def issue():
    global ticket_id
    
    data=request.json
    user_issue = data["issue"].lower()

    category= classify_intent(user_issue)

    if category=="Network issue":
        solution="Please check your internet connection and restart the VPN."
    elif category=="Access issue":
        solution="Please try resetting your password or contact IT support."
    elif category=="Hardware issue":
        solution="Please restart your laptop and close unused applications."
    else:
        solution="Your issue has been noted. IT support will contact you."

    ticket={
        "ticket_id"=ticket_id,
        "issue"=user_issue,
        "category"=category,
        "status"="open",
        "suggested_solution"=solution
    }
    ticket_id +=1
return ticket
   

