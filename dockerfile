# Use a Python base image for building the app
FROM python:3.12-slim as builder

# Set the working directory for the application
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Use a minimal base image for the final production container
FROM python:3.12-slim

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --group appgroup appuser

# Copy the installed packages and application code from the builder stage
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /app /app

# Set the working directory for the final image
WORKDIR /app

# Set environment variables for the application
ENV PORT 8000
ENV PYTHONUNBUFFERED=1

# Change the user to the newly created non-root user
USER appuser

# Expose the application port
EXPOSE 8000

# Run the Django application with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]