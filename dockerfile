# Usamos Python 3.11
FROM python:3.11-slim

# Crear directorio de la app
WORKDIR /app

# Copiar archivos de la app
COPY server.py index.html style.css script.js /app/

# Exponer puerto
EXPOSE 8080

# Instalar dependencias (Flask)
RUN pip install --no-cache-dir flask

# Comando de arranque
CMD ["python", "server.py"]
