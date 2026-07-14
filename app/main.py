from fastapi import FastAPI


app = FastAPI(
    title="Service Desk Uptime Monitor",
    description="API para monitorizar la disponibilidad de servicios.",
    version="0.1.0",
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