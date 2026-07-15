from fastapi import FastAPI

from app.monitor import check_url
from app.schemas import URLCheckRequest, URLCheckResponse


app = FastAPI(
    title="Service Desk Uptime Monitor",
    description="API para monitorizar la disponibilidad de servicios.",
    version="0.3.0",
)


@app.get("/")
def home() -> dict[str, str]:
    return {
        "application": "Service Desk Uptime Monitor",
        "status": "running",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy",
    }

@app.get("/version")
def version() -> dict[str, str]:
    return {
        "version": "0.3.0",
    }


@app.post(
    "/check",
    response_model=URLCheckResponse,
)
async def check_service(
    request: URLCheckRequest,
) -> URLCheckResponse:
    result = await check_url(
        str(request.url),
    )

    return URLCheckResponse(
        **result,
    )