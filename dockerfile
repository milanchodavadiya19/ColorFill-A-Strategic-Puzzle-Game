FROM python:3.8-slim-buster
# :1.10.1-alpine

# Set the working directory
WORKDIR /app

COPY src /app

# Copy the requirements file and install the dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

# Set the entrypoint command
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
