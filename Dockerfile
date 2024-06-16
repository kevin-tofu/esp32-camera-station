FROM python:3.10-slim-buster

WORKDIR /app
COPY ./ ./

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install curl -y
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN poetry install --no-root

# CMD ['poetry', 'run', 'python', './esp32-camera-station']
# CMD ['${HOME}/.local/bin/poetry', 'run', 'python', './main.py']
CMD poetry run python esp32-camera-station
