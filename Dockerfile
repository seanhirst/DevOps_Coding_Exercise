# Use a lightweight base image with Python 3 and Alpine Linux
FROM python:3-alpine3.11

# Install build dependencies including Rust and cargo. 
RUN apk add --no-cache build-base musl-dev rust cargo

# Set the working directory within the container 
WORKDIR /app

# Copy only the necessary files (requirements.txt) to take advantage of Docker layer caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Install Gunicorn (the WSGI server)
RUN pip install gunicorn

# Copy the application code, including the module directory
COPY node_pod_grouper/ ./node_pod_grouper/ 

# Expose the port on which the application will listen
EXPOSE 8080

# Command to start the Gunicorn server with Uvicorn workers, specifying the module path
CMD ["gunicorn", "node_pod_grouper.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]
