# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed dependencies
# Using --no-cache-dir to keep the image size smaller
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local 'app' directory (containing your FastAPI application)
# to the '/app/app' directory in the container
COPY ./app ./app

# Copy the local 'model' directory (containing your skin_model.pth)
# to the '/app/model' directory in the container
COPY ./model ./model

# Make port 8000 available to the world outside this container
# This is the default port Uvicorn and FastAPI use
EXPOSE 8000

# Command to run the Uvicorn server when the container launches
# It will look for an 'app' instance in the 'app.main' module
# The 'app.main' module refers to /app/app/main.py
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]