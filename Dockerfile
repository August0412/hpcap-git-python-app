# Use the official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask app and templates folder into the container
COPY calc.py .
COPY templates/ /app/templates/

# Expose the container's port 5000
EXPOSE 5000

# Command to run the app when the container starts
CMD ["python", "calc.py"]
