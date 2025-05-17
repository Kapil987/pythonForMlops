# Importing Flask class from the flask module
# Ref https://flask.palletsprojects.com/en/stable/quickstart/
from flask import Flask
from flask import Flask, render_template, request

'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''

# Creating a Flask web application instance
app = Flask(__name__)

# Defining a route for the home ('/') URL
## 1 Routes are the path which you enter in browser
# @app.route('/')

## 2
# @app.route("/", methods=["GET"]) 
@app.route("/", methods=["GET", "POST"]) 

## 3
# @app.route("/", methods=["POST"]) # ERROR in browser check this in postman
def hello():
    # Function that returns "Hello, World!" when the home page is accessed
    # return "<h1>Hello, World! 23<h1>"
    # return "Hello, World! any messaage"
    return render_template("index.html")

# Running the application only if this script is executed directly
# if __name__ == '__main__':

# Start the Flask development server with debug mode enabled
app.run(debug=True)