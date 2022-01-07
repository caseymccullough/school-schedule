from flask_app import app
from flask import render_template, request, redirect
from ..models.Student import Student

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/students')
def students():
   return render_template("students.html", all_students = Student.get_all())

@app.route('/create/student', methods=['POST'])
def create_student():
   data = {
      "first_name" : request.form['first_name'],
      "last_name" : request.form['last_name'],
      "grade" : request.form['grade'],
   }
   user_id = Student.save(data)
   return redirect('/students')