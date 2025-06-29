from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    """
    Returns a simple 'Hello, Dockerized Flask App!' message when the root URL is accessed.
    """
    return '<h1>Hello, Dockerized Flask App!<h1>'

# This block ensures the application runs only when the script is executed directly
if __name__ == '__main__':
    # Run the Flask app
    # host='0.0.0.0' makes the server accessible from any IP,
    # which is crucial when running inside a Docker container.
    # port=5000 is the default Flask port, which we will expose in Docker.
    app.run(host='0.0.0.0', port=5000)