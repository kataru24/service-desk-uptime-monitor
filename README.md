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