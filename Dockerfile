FROM python:3.14-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir \
    -r /code/requirements.txt \
    && groupadd --gid 10001 appuser \
    && useradd \
    --uid 10001 \
    --gid appuser \
    --no-create-home \
    --shell /usr/sbin/nologin \
    appuser

COPY --chown=appuser:appuser app /code/app

USER appuser

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]