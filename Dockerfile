FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt ./
# Evitar la ejecución de scripts de configuración al instalar paquetes
# forzando el uso de ruedas binarias cuando sea posible.
# Si algún paquete no ofrece rueda, la instalación fallará; en ese caso
# considerar usar ruedas preparadas o permitir paquetes fuente de confianza.
RUN pip install --no-cache-dir --only-binary=:all: -r requirements.txt

# Copiar aplicación de forma selectiva para evitar añadir datos confidenciales
# Copiar sólo los ficheros necesarios al contenedor
COPY main.py ./
# Si añade módulos o paquetes, copie las carpetas necesarias, por ejemplo:
# COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
