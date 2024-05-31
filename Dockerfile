# Use a lightweight base image with Python 3 and Alpine Linux
FROM python:3-alpine3.11

# Set the working directory within the container 
WORKDIR /app

# Copy only the necessary files (requirements.txt) to take advantage of Docker layer caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt

# Install Gunicorn (the WSGI server)
RUN pip install gunicorn

# Copy the rest of the application code
COPY . .

# Expose the port on which the application will listen
EXPOSE 8080

# Command to start the Gunicorn server with Uvicorn workers
CMD ["gunicorn", "main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]