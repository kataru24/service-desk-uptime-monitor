FROM python:3.14-slim-bookworm

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir \
    -r /code/requirements.txt

COPY app /code/app

EXPOSE 8000

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]