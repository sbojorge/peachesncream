#!/bin/bash

# This script is executed when the Docker container starts in Cloud Run.

# Apply database migrations.
# `--noinput` prevents Django from prompting for confirmation during migrations,
# which is essential for automated deployments.
echo "Applying database migrations..."
python manage.py migrate --noinput

# Collect static files.
# For Cloud Run, it's common to serve static files directly from Google Cloud Storage
# or a CDN. This `collectstatic` command gathers all static files into your
# `STATIC_ROOT` directory, which can then be uploaded to GCS (e.g., as part of your CI/CD,
# or if your `STATICFILES_STORAGE` is configured to upload directly to GCS).
# `--noinput` prevents prompts.
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Gunicorn web server.
# Gunicorn is a robust WSGI HTTP server for Unix, commonly used for Django in production.
# `--bind :$PORT` tells Gunicorn to listen on all network interfaces on the port
# specified by the `PORT` environment variable, which Cloud Run automatically provides.
# `--workers 2` sets the number of worker processes. Adjust based on your app's needs.
# `--timeout 60` sets the worker timeout in seconds.
# `YOUR_PROJECT_NAME.wsgi:application` points to your Django project's WSGI application.
# Replace `YOUR_PROJECT_NAME` with the actual name of your Django project
# (the directory containing `settings.py` and `wsgi.py`).
echo "Starting Gunicorn server..."
exec gunicorn --bind :$PORT --workers 2 --timeout 60 main.wsgi:application
