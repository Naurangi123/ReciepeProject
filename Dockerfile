FROM python:3.12-alpine3.19
LABEL maintainer="naurangi"

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
COPY requirements.dev.txt .

RUN pip install -r requirements.txt

RUN pip install --upgrade flake8

COPY ./app app
WORKDIR /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip 
RUN /py/bin/pip install -r /requirements.txt  
RUN if [ $DEV = "true" ];  \
    then /py/bin/pip install -r /requirements.dev.txt; \
    fi
RUN adduser -D -H django-user

ENV PATH="/py/bin:$PATH"

USER django-user

