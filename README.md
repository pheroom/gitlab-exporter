# GitLab Prometheus Exporter

Simple web service to export metrics from GitLab to Prometheus.

## Running

1. Install the [required](pyproject.toml) Python version.
1. Install the latest [Poetry](https://python-poetry.org/docs/) version.
1. Install the exporter package.
   ```shell
   poetry install
   ```
1. Run the service.
   ```shell
   poetry run uvicorn gitlab_prom_exporter:app
   ```
1. Configure a webhook in GitLab project settings.
   - URL: `<exporter URL>/api/gitlab/event`
   - Trigger: Job events.

## Development

Before committing your changes, run the code quality tools and fix any errors.
```shell
poetry run ruff check
poetry run ruff format
poetry run mypy .
