# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable for service account file path
ENV GOOGLE_APPLICATION_CREDENTIALS /app/udp-mhacks23-10.json

# Run app.py when the container launches
CMD ["python", "doc_app.py"]