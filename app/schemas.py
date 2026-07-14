from pydantic import BaseModel, HttpUrl


class URLCheckRequest(BaseModel):
    url: HttpUrl


class URLCheckResponse(BaseModel):
    url: str
    reachable: bool
    healthy: bool
    status_code: int | None = None
    latency_ms: float | None = None
    error: str | None = None