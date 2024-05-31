# Use a lightweight base image with Python 3 and Alpine Linux
FROM python:3-alpine3.11

# Install build dependencies including Rust and cargo. 
RUN apk add --no-cache build-base musl-dev

# Update Rust to ensure compatibility
# Install rustup (the Rust toolchain installer)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
# Add Cargo's bin directory to PATH (replace /root/.cargo/bin with the actual path if it's different)
ENV PATH="/root/.cargo/bin:${PATH}"

# Set the working directory within the container
WORKDIR /app

# Make a node_pod_grouper directory
RUN mkdir /app/node_pod_grouper

# Copy the files into the created directory 
COPY requirements.txt node_pod_grouper/__init__.py node_pod_grouper/main.py node_pod_grouper/node_pod_grouper.py /app/node_pod_grouper/

# Upgrade pip first to ensure latest version
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install -r node_pod_grouper/requirements.txt --no-cache-dir

# Install Gunicorn (the WSGI server)
RUN pip install gunicorn

# Expose the port on which the application will listen
EXPOSE 8080

# Command to start the Gunicorn server with Uvicorn workers, specifying the module path
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080", "node_pod_grouper.main:app"]
