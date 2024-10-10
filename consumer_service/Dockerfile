FROM python:3.11

RUN apt-get update && apt-get install -y build-essential libpq-dev

RUN pip install poetry

RUN curl https://pyenv.run | bash

WORKDIR /app

COPY . .

RUN poetry install
