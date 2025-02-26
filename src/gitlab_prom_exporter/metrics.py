"""
Definitions of Prometheus metrics and their labels.
"""

from prometheus_client import Counter
from pydantic import BaseModel


class JobEventsLabels():
    project: str
    job: str
    ref: str
    user: str
    status: str


class Metrics:
    job_events = Counter(
        name="gitlab_ci_job_events_total",
        documentation="Total number of GitLab CI/CD job events",
    )