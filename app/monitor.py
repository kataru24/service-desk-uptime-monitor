import time

import httpx


async def check_url(url: str) -> dict:
    start_time = time.perf_counter()

    try:
        async with httpx.AsyncClient(
            follow_redirects=True,
            timeout=10.0,
        ) as client:
            response = await client.get(url)

        latency_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )

        return {
            "url": str(response.url),
            "reachable": True,
            "healthy": 200 <= response.status_code < 400,
            "status_code": response.status_code,
            "latency_ms": latency_ms,
            "error": None,
        }

    except httpx.RequestError as exception:
        latency_ms = round(
            (time.perf_counter() - start_time) * 1000,
            2,
        )

        return {
            "url": url,
            "reachable": False,
            "healthy": False,
            "status_code": None,
            "latency_ms": latency_ms,
            "error": exception.__class__.__name__,
        }