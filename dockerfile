# Stage 1: Build Stage
FROM python:3.12-slim as builder

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for your application
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Stage 2: Production Stage
FROM python:3.12-slim

# Set environment variables again
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose the port Cloud Run will use
EXPOSE 8000

# Create a user to run the app
RUN addgroup --system appgroup && adduser --system --group appgroup appuser
USER appuser

# Set the working directory
WORKDIR /app

# Copy the application code and installed packages from the builder stage
COPY --chown=appuser:appgroup --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --chown=appuser:appgroup . .

# Run collectstatic to prepare static files
RUN python manage.py collectstatic --noinput

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "your_project_name.wsgi:application"]