# Use a slim Python image for a smaller final image size.
# Using a specific version (e.g., 3.9, 3.10, 3.11) is recommended for stability.
FROM python:3.11-slim-buster

# Set environment variables for non-sensitive configurations.
# PYTHONUNBUFFERED ensures that Python's stdout and stderr are not buffered,
# which is helpful for seeing logs in real-time in Cloud Run.
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for `mysqlclient` and other potential build tools.
# `default-libmysqlclient-dev` provides development headers for the MySQL client library,
# which `mysqlclient` needs to compile.
# `gcc` and `build-essential` are general compilation tools.
# `rm -rf /var/lib/apt/lists/*` cleans up apt cache to reduce image size.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        default-libmysqlclient-dev \
        gcc \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Copy the `requirements.txt` file into the container.
# This step is done separately to leverage Docker's layer caching.
# If only your application code changes, but `requirements.txt` doesn't,
# Docker won't re-run the `pip install` command, speeding up builds.
COPY requirements.txt .

# Install Python dependencies from `requirements.txt`.
# `--no-cache-dir` prevents pip from storing its cache, further reducing image size.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Django application code into the container.
# The `.` at the end means "copy everything from the current directory on the host
# to the current working directory in the container (`/app`)".
COPY . .


# Make the `run.sh` script executable.
# This script will be our entrypoint to manage startup tasks.
RUN chmod +x /app/run.sh

# Expose the port that the application will listen on.
# Cloud Run automatically sets the `PORT` environment variable, usually to 8080.
# While `EXPOSE` doesn't publish the port, it serves as documentation.
EXPOSE 8080

# Define the command to run when the container starts.
# This executes our `run.sh` script, which handles migrations and starts the server.
CMD ["/app/run.sh"]