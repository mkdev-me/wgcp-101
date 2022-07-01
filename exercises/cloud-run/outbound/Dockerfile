FROM python:3.9-slim

RUN apt-get update && apt-get install -y iputils-ping curl

ENV PYTHONUNBUFFERED True

COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY *.py ./

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
