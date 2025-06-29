# Use an official Python runtime as a parent image.
# python:3.9-slim-buster is a good choice for its small size and stability.
FROM python:3.9-slim-buster

# Set the working directory inside the container.
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Copy the requirements.txt file into the container's /app directory.
# This step is done early to take advantage of Docker's layer caching.
# If requirements.txt doesn't change, this layer (and the pip install) can be reused.
COPY requirements.txt .

# Install the Python dependencies listed in requirements.txt.
# --no-cache-dir prevents pip from storing cache, reducing the final image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container's /app directory.
# This includes your app.py file.
COPY . /app

# Expose port 5000. This informs Docker that the container listens on this port
# at runtime. It doesn't actually publish the port; that's done with `docker run -p`
# or in `docker-compose.yml`.
EXPOSE 5000

# Define the command to run the application when the container starts.
# This will execute app.py using Python.
CMD ["python", "app.py"]
