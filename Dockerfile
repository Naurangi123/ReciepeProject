
# FROM python:3.12-alpine
# LABEL maintainer="naurangi"


# ENV PYTHONUNBUFFERED=1
# ENV PATH="/py/bin:$PATH"

# COPY ./requirements.txt .
# COPY ./requirements.dev.txt .
# COPY ./app /app
# WORKDIR /app
# EXPOSE 8000




# ARG DEV=false

# RUN python -m venv /py
# RUN /py/bin/pip install --upgrade pip
# RUN apk add --update --no-cache postgresql-client
# RUN apk add --update --virtual build-deps \
#         build-base postgresql-dev musl-dev
# RUN pip install psycopg2 
# RUN /py/bin/pip install -r requirements.txt 
# RUN if [ "$DEV" = "true" ]; then /py/bin/pip install -r requirements.dev.txt; fi 

# # Install additional tools
# RUN apk del build-deps

# # Create and use a non-root user
# RUN adduser -D -H django-user
# USER django-user

FROM python:3.12-alpine
LABEL maintainer="naurangi"

ENV PYTHONUNBUFFERED=1
ENV PATH="/py/bin:$PATH"

# Create and use a non-root user
RUN adduser -D -H django-user

# Set work directory and copy necessary files
WORKDIR /app
COPY ./requirements.txt ./requirements.dev.txt ./app /app/

# Install dependencies and tools
RUN python -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && apk add --update --no-cache postgresql-client \
    && apk add --update --virtual build-deps build-base postgresql-dev musl-dev \
    && /py/bin/pip install psycopg2 \
    && /py/bin/pip install -r requirements.txt \
    && if [ $DEV = "true" ]; then /py/bin/pip install -r requirements.dev.txt; fi \
    && apk del build-deps

EXPOSE 8000

USER django-user
