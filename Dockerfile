# Use the official Python image with Alpine Linux
FROM python:3.12-alpine
LABEL maintainer="naurangi"

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PATH="/py/bin:$PATH"

# Create a virtual environment
RUN python -m venv /py

# Upgrade pip
RUN /py/bin/pip install --upgrade pip

RUN /py/bin/pip install --upgrade pip setuptools wheel

# Copy requirements files into the container
COPY requirements.txt .
COPY requirements.dev.txt .

# Install runtime dependencies
RUN /py/bin/pip install -r requirements.txt

# Install development tools and additional dependencies if needed
ARG DEV=false
RUN apk add --no-cache --virtual .tmp-build-deps \
    build-base \
    postgresql-dev \
    musl-dev \
    && if [ "$DEV" = "true" ]; then /py/bin/pip install -r requirements.dev.txt; fi \
    && apk del .tmp-build-deps

# Install additional tools
RUN apk add --no-cache postgresql-client

# Copy application code into the container
COPY ./app /app

# Set working directory
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Create and use a non-root user
RUN adduser -D -H django-user
USER django-user

