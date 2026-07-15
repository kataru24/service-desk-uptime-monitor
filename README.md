## Usar la imagen publicada

La imagen Docker se publica automáticamente en GitHub Container Registry después de superar las pruebas del pipeline.

Descargar la última versión:

```bash
docker pull ghcr.io/kataru24/service-desk-uptime-monitor:latest
```

Ejecutar la imagen:

```bash
docker run --detach \
  --rm \
  --name uptime-monitor-ghcr \
  --publish 8000:8000 \
  ghcr.io/kataru24/service-desk-uptime-monitor:latest
```

Comprobar el estado:

```bash
curl http://localhost:8000/health
```

Detener el contenedor:

```bash
docker stop uptime-monitor-ghcr
```

## Ejecutar con Docker

Construir la imagen:

```bash
docker build -t service-desk-uptime-monitor:0.2.0 .
```

Ejecutar el contenedor:

```bash
docker run --detach \
  --rm \
  --name service-desk-uptime-monitor \
  --publish 8000:8000 \
  service-desk-uptime-monitor:0.2.0
```

Comprobar el estado:

```bash
curl http://localhost:8000/health
```

Abrir la documentación:

```text
http://localhost:8000/docs
```

Detener el contenedor:

```bash
docker stop service-desk-uptime-monitor
```

## Ejecutar las pruebas

Con el entorno virtual activado, ejecutar:

```bash
python -m pytest -v

# Service Desk Uptime Monitor

Aplicación web desarrollada para monitorizar la disponibilidad de servicios y medir sus tiempos de respuesta

## Estado del proyecto

Work In Progress

## Funcionalidades actuales

- API desarrollada con FastAPI
- Endpoint principal de estado
- Endpoint de health check
- Documentación interactiva mediante Swagger UI

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Muestra información básica de la aplicación |
| GET | `/health` | Comprueba el estado de la aplicación |

## Tecnologías

- Python
- FastAPI
- Git
- WSL 2
- Ubuntu

## Ejecutar el proyecto

Crear un entorno virtual:

```bash
python3 -m venv .venv