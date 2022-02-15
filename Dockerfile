FROM python:3.10.2-slim-buster

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-interaction


COPY ./migrations /migrations
COPY ./src /app
