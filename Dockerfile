# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files into container
COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY backend/listings.json ./backend/

# Install dependencies
RUN pip install flask flask-cors

# Set environment variables
ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
