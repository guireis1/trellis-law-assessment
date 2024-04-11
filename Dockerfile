# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install poetry
RUN pip install --no-cache-dir poetry

# Copy the project files into the container
COPY pyproject.toml poetry.lock ./

# Install the project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of your application's code
COPY . .

# Run the application
CMD poetry run python main.py