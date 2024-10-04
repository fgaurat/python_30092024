from flask import Flask,render_template
from EmployeeDAO import EmployeeDAO
import time
app = Flask(__name__)

@app.route("/helloworld")
def hello_world():

    return f"<p>Hello, World! {int(time.time())}</p>"

@app.route("/moche")
def mocheindex():
    dao = EmployeeDAO("employees_db.db")
    employees = dao.find_all()
    table = "<table>"
    table+= "<thead>"
    table+= "<tr>"
    table+= "<th>#</th><th>firstname</th><th>lastname</th>"
    table+= "</tr>"
    table+= "</thead>"
    table+= "<tbody>"
    for employee in employees:
        table+= "<tr>"
        table+= f"<td>{employee.id}</td>"
        table+= f"<td>{employee.first_name}</td>"
        table+= f"<td>{employee.last_name}</td>"
        table+= "</tr>"
    table+= "</tbody>"
    
    
    
    table+= "</table>"
    return table

@app.route("/")
def index():
    dao = EmployeeDAO("employees_db.db")
    employees = dao.find_all()
    return render_template('employees.html',employees = employees)
