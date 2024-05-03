FROM tecktron/python-waitress:python-3.12-slim

ENV APP_MODULE="app:app"

COPY ./src /app

RUN ["pip", "install", "-r", "requirements.txt"]
