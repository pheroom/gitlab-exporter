FROM python:3.13

RUN apt-get update && apt-get install -y \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean

RUN pip install poetry && \
    poetry --version

WORKDIR /app

COPY . /app/

RUN poetry install --no-interaction

CMD ["poetry", "run", "uvicorn", "gitlab_prom_exporter:app", "--host", "0.0.0.0", "--port", "8000"]
