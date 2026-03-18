Clinic Queue Manager System
A web-based clinic queue management system built using Python Flask.
This project demonstrates key concepts in Object-Oriented Programming (OOP) and Data Structures such as Queue (FIFO) and Stack (LIFO).

Project Overview
The system allows clinic staff to:
Sign in using their name (no password required,i.e any name of choice)
Add patients to a waiting queue
Serve patients in order (First-In-First-Out)
View previously served patients
Track total number of patients in queue

**Features**
Simple Sign-In (Name only)
Add Patients to Queue
FIFO Queue Management
Serve Next Patient
Patient Counter
Served Patients History (Stack)
Timestamp for each patient
Clean and responsive user interface
Doctor image on login page
Clinic logo on dashboard

Queue (FIFO)
Used to manage patients waiting in line.
Operations:
append() → Add patient
popleft() → Serve patient

Stack (LIFO)
Used to store served patients.
Operations:
append() → Add served patient
pop() → Remove last served patient

Technologies Used
Python
Flask
HTML
CSS
collections.deque
Git & GitHub

Project Structure
clinic_queue_manager/
│
├── app.py
├── models.py
├── README.md
│
├── static/
│   ├── style.css
│   ├── logo.png
│   └── doctor.png
│
└── templates/
    ├── login.html
    └── index.html
How to Run the Project
1. Install Flask
pip install flask
2. Run the application
python app.py
3. Open in browser
http://127.0.0.1:5000.

**Academic Purpose**
This project was developed for CSC 202 Continuous Assessment to demonstrate:
Object-Oriented Programming
Queue (FIFO)
Stack (LIFO)
Web development using Flask

 **Author
Amina Ali Haruna
✅ Status
✔ Completed
✔ Ready for submission
✔ Fully functional**
