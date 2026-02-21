# syntax=docker/dockerfile:1

# Use the official Python 3.14 slim image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install Python dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Expose port (FastAPI default)
EXPOSE 80

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
