from flask_app import app
from flask_app.controllers import students
from flask import render_template

if __name__ == "__main__":
    app.run(debug=True)

