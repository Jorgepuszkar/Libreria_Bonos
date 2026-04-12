FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the library
COPY . .

# Install the library
RUN pip install --no-cache-dir -e .

# Install additional tools for development
RUN pip install --no-cache-dir pytest jupyter jupyterlab matplotlib

# Create notebooks directory
RUN mkdir -p /workspace/notebooks

# Default to Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
