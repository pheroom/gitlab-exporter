from fastapi import FastAPI, Request, Response, status
from prometheus_client import make_asgi_app as make_prometheus_app
from pydantic import ValidationError

from gitlab_prom_exporter.metrics import JobEventsLabels, Metrics
from gitlab_prom_exporter.schemas import JobEvent

app = FastAPI(title="gitlab-prom-exporter")
app.mount("/api/metrics", make_prometheus_app())

@app.get("/")
async def read_root():
    return {"message": "App work"}

@app.post("/api/gitlab/event")
async def post_gitlab_event(request: Request) -> Response:
    event_type = request.headers.get("X-Gitlab-Event")
    if event_type == "Job Hook":
        try:
            event = JobEvent.model_validate_json(await request.body())
        except ValidationError as e:
            return Response(f"Invalid event: {e}", status.HTTP_400_BAD_REQUEST)
        labels = JobEventsLabels(
            project=event.project.path_with_namespace,
            job=event.build_name,
            ref=event.ref,
            user=event.user.username,
            status=event.build_status,
        )
        Metrics.job_events.labels(**labels.model_dump()).inc()
        return Response()
    else:
        return Response(f"Unsupported event: {event_type}", status.HTTP_400_BAD_REQUEST)