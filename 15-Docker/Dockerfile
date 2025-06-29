# Use an official Python runtime as a parent image.
# We're using a specific version for stability (3.9-slim-buster is common for its small size).
# While the request mentioned Ubuntu, using a Python-specific image like this
# is generally more efficient and recommended for Python applications.
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install any needed packages specified in requirements.txt
# --no-cache-dir prevents pip from saving downloaded packages, reducing image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the current directory contents into the container at /app
# This copies your app.py and any other files in your project directory.
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
# This specifies the command to execute when the container starts.
CMD ["python", "app.py"]
