FROM ubuntu:18.04

# Python output is sent straight to terminal
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN mkdir /app

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3.8 python3-pip python3.8-dev libpython3.8-dev libmysqlclient-dev

RUN pip3 install pipenv

COPY Pipfile /app/Pipfile

COPY Pipfile.lock /app/Pipfile.lock

RUN pipenv sync

COPY . /app

COPY ./compose/production/django/start.sh ./start.sh

RUN chmod +x ./start.sh