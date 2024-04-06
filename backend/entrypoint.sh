#!/bin/bash

# Wait for the database service to be ready
until python manage.py check; do
  echo "Waiting for database to be ready..."
  sleep 2
done

# Apply migrations
python manage.py migrate

# Start the Django development server
exec "$@"
