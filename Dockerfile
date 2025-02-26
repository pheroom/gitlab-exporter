FROM python:3.13

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY . /app/

RUN poetry install --no-interaction

CMD ["poetry", "run", "uvicorn", "gitlab_prom_exporter:app", "--host", "0.0.0.0", "--port", "8000"]
