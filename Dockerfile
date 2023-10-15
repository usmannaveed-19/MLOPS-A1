# Use an official Python runtime as a base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the application source code and test cases into the container
COPY A1.py .
COPY test.py .

# Define the command to run your application (A1.py)
CMD ["python", "A1.py"]
