# app.py

from flask import Flask
import pymongo # Import the PyMongo library for MongoDB
import time    # For pausing execution
import threading # For running the DB check in a separate thread
import logging # For logging status messages

# Configure basic logging to output to the console (Docker logs)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a Flask web application instance
app = Flask(__name__)

# MongoDB connection details
# 'db' is the service name defined for MongoDB in your docker-compose.yml.
# Docker Compose creates a network where service names resolve to their IPs.
MONGO_HOST = 'db'
MONGO_PORT = 27017

def check_mongodb_status():
    """
    Continuously checks MongoDB connection status every 2 seconds and logs it.
    This function runs in a separate thread to avoid blocking the Flask web server.
    """
    while True:
        try:
            # Attempt to establish a connection to MongoDB
            # serverSelectionTimeoutMS: Limits the time the driver will wait to find a server
            client = pymongo.MongoClient(MONGO_HOST, MONGO_PORT, serverSelectionTimeoutMS=1000)
            # The ping command is a lightweight way to check if the database is reachable and responsive.
            client.admin.command('ping')
            logging.info("MongoDB connection: SUCCESSFUL")
            client.close() # It's good practice to close the client after the check if not continuously used.
        except pymongo.errors.ConnectionFailure as e:
            # Log an error if the connection fails (e.g., MongoDB is not yet up or unreachable)
            logging.error(f"MongoDB connection: FAILED - {e}")
        except Exception as e:
            # Catch any other unexpected errors during the check
            logging.error(f"An unexpected error occurred during MongoDB check: {e}")
        
        # Wait for 2 seconds before performing the next check
        time.sleep(2) 

@app.route('/')
def hello_world():
    """
    Returns a simple message indicating the Flask app is running and DB status
    is being logged in the background.
    """
    return 'Hello from Flask! MongoDB connection status is being logged in the background.'

# This block ensures the application runs only when the script is executed directly
if __name__ == '__main__':
    # Start the MongoDB status check function in a separate thread.
    # db_checker_thread.daemon = True ensures that the thread will
    # exit automatically when the main program (Flask app) exits.
    db_checker_thread = threading.Thread(target=check_mongodb_status)
    db_checker_thread.daemon = True
    db_checker_thread.start()

    # Run the Flask app
    # host='0.0.0.0' makes the server accessible from any IP,
    # which is crucial when running inside a Docker container.
    # port=5000 is the default Flask port.
    app.run(host='0.0.0.0', port=5000)
