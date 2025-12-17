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
    network_examples = [
        "vpn not working",
        "internet connection issue",
        "cannot connect to network",
        "remote access problem"
    ]

    access_examples = [
        "forgot password",
        "login failed",
        "account locked",
        "cannot access system"
    ]

    hardware_examples = [
        "laptop is slow",
        "system hangs",
        "computer overheating",
        "device not responding"
    ]

    def similarity(text, examples):
        score = 0
        for example in examples:
            for word in example.split():
                if word in text:
                    score += 1
        return score

    scores = {
        "Network Issue": similarity(user_issue, network_examples),
        "Access Issue": similarity(user_issue, access_examples),
        "Hardware Issue": similarity(user_issue, hardware_examples)
    }

    best_category = max(scores, key=scores.get)

    if scores[best_category] == 0:
        return "General IT Issue"

    return best_category


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
        "ticket_id":ticket_id,
        "issue":user_issue,
        "category":category,
        "status":"open",
        "suggested_solution":solution
    }
    ticket_id +=1
return ticket
   

