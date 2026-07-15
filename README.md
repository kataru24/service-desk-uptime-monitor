## Seguridad del contenedor y Kubernetes

La aplicación se ejecuta utilizando un usuario sin privilegios tanto en Docker como en Kubernetes.

Medidas aplicadas en la imagen Docker:

- Usuario dedicado `appuser`.
- UID y GID fijos: `10001`.
- Ejecución del proceso sin permisos de `root`.
- Propiedad de los archivos asignada al usuario de la aplicación.
- Generación de archivos `.pyc` deshabilitada.

Medidas aplicadas en Kubernetes:

- Ejecución obligatoria como usuario no-root.
- UID y GID `10001`.
- Escalada de privilegios deshabilitada.
- Todas las capacidades Linux eliminadas.
- Sistema de archivos raíz configurado como solo lectura.
- Perfil seccomp `RuntimeDefault`.
- Montaje automático del token de Service Account deshabilitado.
- Requests y limits de CPU y memoria.

Las restricciones se validaron directamente dentro de los Pods.

Comprobar el usuario del contenedor:

```bash
kubectl exec \
  --namespace uptime-monitor \
  POD_NAME \
  -- id
```

Resultado esperado:

```text
uid=10001(appuser) gid=10001(appuser) groups=10001(appuser)
```

Comprobar capacidades y escalada de privilegios:

```bash
kubectl exec \
  --namespace uptime-monitor \
  POD_NAME \
  -- sh -c 'grep -E "^(NoNewPrivs|CapEff):" /proc/1/status'
```

Resultado esperado:

```text
CapEff:         0000000000000000
NoNewPrivs:     1
```

Comprobar que el sistema de archivos raíz es de solo lectura:

```bash
kubectl exec \
  --namespace uptime-monitor \
  POD_NAME \
  -- sh -c 'echo test > /code/security-test'
```

El comando debe fallar con un mensaje similar a:

```text
Read-only file system
```

## Desplegar en Kubernetes

El proyecto incluye manifiestos para desplegar la aplicación en un clúster Kubernetes.

La arquitectura utiliza:

- Un namespace dedicado.
- Un Deployment con dos réplicas.
- Readiness y liveness probes.
- Límites y solicitudes de recursos.
- Un Service de tipo ClusterIP.

Aplicar los manifiestos:

```bash
kubectl apply -f kubernetes/namespace.yaml

kubectl apply -f kubernetes/deployment.yaml

kubectl apply -f kubernetes/service.yaml
```

Comprobar el estado del despliegue:

```bash
kubectl rollout status \
  deployment/service-desk-uptime-monitor \
  --namespace uptime-monitor
```

Mostrar los Pods:

```bash
kubectl get pods --namespace uptime-monitor
```

Acceder temporalmente a la aplicación:

```bash
kubectl port-forward \
  --namespace uptime-monitor \
  service/service-desk-uptime-monitor \
  8080:8000
```

Abrir la documentación:

```text
http://localhost:8080/docs
```

Comprobar el health check:

```bash
curl http://localhost:8080/health
```

## Usar la imagen publicada

La imagen Docker se publica automáticamente en GitHub Container Registry después de superar las pruebas del pipeline

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