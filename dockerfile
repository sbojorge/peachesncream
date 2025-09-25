# Use a Python base image for building and running the app
FROM python:3.12-slim

# Set the working directory for the application
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Create a non-root group and user
RUN groupadd --system appgroup && useradd --system --gid appgroup appuser

# Copy application code
COPY . /app

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Change the user to the newly created non-root user
USER appuser

# Set environment variables for the application
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

# Expose the application port
EXPOSE 8000

# Run the Django application with Gunicorn, using the PORT environment variable
CMD gunicorn --bind 0.0.0.0:${PORT} main.wsgi:application

