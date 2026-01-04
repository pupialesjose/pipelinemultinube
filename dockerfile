FROM python:3.11-slim

WORKDIR /app

# Instalar cliente sqlite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App
COPY . .

EXPOSE 8080

CMD ["python", "server.py"]
