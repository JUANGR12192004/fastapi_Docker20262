FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación de forma selectiva para evitar añadir datos confidenciales
# Copiar sólo los ficheros necesarios al contenedor
COPY main.py ./
# Si añade módulos o paquetes, copie las carpetas necesarias, por ejemplo:
# COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
