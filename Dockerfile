FROM python:3.6.7-stretch

ENV FLASK_APP=app.py

COPY . /app
WORKDIR /app

RUN sh -c "pip install -r requirements.txt"

EXPOSE 8000