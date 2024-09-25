#!/bin/sh

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting the application..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
