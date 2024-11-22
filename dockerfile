# Set the Python version as a build-time argument
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH=/opt/venv/bin:$PATH

# Upgrade pip
RUN pip install --upgrade pip

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev libjpeg-dev libcairo2 gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Copy project files
COPY . /code

# Install project dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Set environment variables
#ARG DJANGO_SECRET_KEY
#ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}

ARG DJANGO_DEBUG=0
ENV DJANGO_DEBUG=${DJANGO_DEBUG}

# Set the Django project name
ARG PROJ_NAME="django_crm"

# Runtime script
RUN printf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --no-input\n" >> ./paracord_runner.sh && \
    printf "python manage.py collectstatic --noinput\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh

# Make the script executable
RUN chmod +x paracord_runner.sh

# Run the project
CMD ["bash", "./paracord_runner.sh"]
