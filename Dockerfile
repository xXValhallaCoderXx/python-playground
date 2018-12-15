FROM python:3.7-slim

# Set environment varibles

# This tell python not to write pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# This ensures console output not buffered by docker
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY ./Pipfile /app/Pipfile
RUN pipenv install --system --skip-lock

# Copy project
COPY . /app/