#clinic queue system using flask
from flask import Flask, render_template, request, redirect, session
from collections import deque
from models import Patient

app = Flask(__name__)
app.secret_key = "clinic_secret"

# FIFO Queue
patient_queue = deque()

# LIFO Stack
served_history = []


# SIGN IN (NO PASSWORD)
@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        session["user"] = username
        return redirect("/home")

    return render_template("login.html")


# HOME PAGE (Dashboard)
@app.route("/home")
def home():

    if "user" not in session:
        return redirect("/")

    patients = [p.get_details() for p in patient_queue]
    history = [p.get_details() for p in served_history]

    total = len(patient_queue)

    return render_template(
        "index.html",
        patients=patients,
        history=history,
        total=total
    )


# ADD PATIENT (from dashboard form)
@app.route("/add", methods=["POST"])
def add_patient():

    if "user" not in session:
        return redirect("/")

    name = request.form["name"]

    patient = Patient(name)

    patient_queue.append(patient)

    return redirect("/home")


# SERVE PATIENT (FIFO)
@app.route("/serve")
def serve():

    if "user" not in session:
        return redirect("/")

    if patient_queue:
        served_patient = patient_queue.popleft()
        served_history.append(served_patient)

    return redirect("/home")


# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
