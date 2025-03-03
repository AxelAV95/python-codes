# Usamos una imagen base oficial de Python con slim para reducir el tamaño
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalamos dependencias del sistema necesarias para PyMySQL y otras librerías
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el archivo de requisitos primero (optimización de caché de Docker)
COPY requirements.txt .

# Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código de la aplicación
COPY . .

# Establecemos las variables de entorno
ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=production

# Exponemos el puerto 5000 (el mismo que usa tu app)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "run.py"]

# Producción
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]