# Servicio FastAPI: obtener_cedula

Endpoint:

- `GET /obtener_cedula` — devuelve un JSON con un número entero aleatorio de 10 dígitos: `{ "cedula": 1234567890 }`.

Instrucciones de ejecución:

1. Crear y activar un entorno virtual (opcional pero recomendado).

```
python -m venv .venv
.venv\Scripts\activate
```

2. Instalar dependencias:

```
pip install -r requirements.txt
```

3. Ejecutar la aplicación con Uvicorn:

```
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

4. Probar el endpoint:

```
curl http://127.0.0.1:8000/obtener_cedula
```

Docker
------

Construir y ejecutar con Docker:

```
docker build -t obtener_cedula .
docker run --rm -p 8000:8000 obtener_cedula
```

Usando Docker Compose:

```
docker compose up --build -d
docker compose down
```

Acceder a la aplicación desde el host
-----------------------------------

- La aplicación expone el puerto `8000` dentro del contenedor y está mapeado al puerto `8000` del host por defecto.
- Swagger UI (interfaz Swagger / OpenAPI): http://127.0.0.1:8000/docs
- ReDoc (documentación alternativa): http://127.0.0.1:8000/redoc
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

Ver logs y estado
------------------

- Ver logs del servicio (Compose):

```
docker compose logs -f
```

- Reconstruir y reiniciar (por cambios de código):

```
docker compose up --build -d
```

Variables de entorno
---------------------

Si necesitas pasar variables de entorno, añade un archivo `.env` o define `environment:` en `docker-compose.yml`.

Colección Postman
-----------------

Se incluye una colección Postman lista para importar en [postman_collection.json](postman_collection.json). Pasos para usarla:

1. Abre Postman.
2. Importa el archivo [postman_collection.json](postman_collection.json).
3. Reemplaza las variables `host` y `port` en la colección si es necesario (por defecto `127.0.0.1` y `8000`).

También puedes importar directamente desde la especificación OpenAPI disponible en `http://127.0.0.1:8000/openapi.json` (Postman soporta importar desde URL).

Swagger (FastAPI)
-----------------

FastAPI expone una UI Swagger en `/docs` y ReDoc en `/redoc`. Estas interfaces son generadas automáticamente a partir de la especificación OpenAPI, por lo que no necesitas crear documentación manualmente.

Archivos relevantes
------------------

- [main.py](main.py) — aplicación FastAPI.
- [Dockerfile](Dockerfile) — imagen para Docker.
- [docker-compose.yml](docker-compose.yml) — levantar el servicio con Docker Compose.
- [postman_collection.json](postman_collection.json) — colección Postman lista para importar.

Despliegue continuo con GitHub Actions y Render
----------------------------------------------

Este repositorio incluye un workflow de GitHub Actions que dispara un despliegue en Render cada vez que se hace `push` a la rama `main`.

Archivo del workflow: `.github/workflows/deploy_render.yml`.

Configuración requerida en GitHub:

1. Ve a `Settings > Secrets and variables > Actions` en tu repositorio.
2. Añade los siguientes secretos:
	- `RENDER_API_KEY` — tu API Key de Render (con permisos para crear deploys).
	- `RENDER_SERVICE_ID` — el `service id` de tu servicio en Render (algo como `srv-...`).

Cómo funciona el workflow:

- En cada `push` a `main`, la acción ejecuta una petición HTTP POST a la API de Render:

```
POST https://api.render.com/v1/services/${{ secrets.RENDER_SERVICE_ID }}/deploys
Authorization: Bearer ${{ secrets.RENDER_API_KEY }}
Content-Type: application/json
Body: {}
```

- Render iniciará la construcción y publicación del servicio según su configuración (Build Command, Start Command, etc.) definida en el panel de Render.

Notas y seguridad
-----------------

- No guardes tu `RENDER_API_KEY` en código ni en archivos públicos. Usa los `Secrets` de GitHub Actions.
- Si prefieres que solo algunos cambios desencadenen el despliegue, modifica la sección `on:` del workflow (por ejemplo, limitar a determinados paths).

Prueba manual
-------------

Puedes probar el endpoint del workflow forzando un push a `main` o creando un commit y abriendo un PR y mergeándolo.



