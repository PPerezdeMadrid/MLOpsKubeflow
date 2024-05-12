# Usa una imagen de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código actual al contenedor en /app
COPY modeloScoring.py .

# Instala las dependencias de Python
RUN pip install --no-cache-dir pandas h2o kfp

# Define el comando por defecto para ejecutar tu aplicación
CMD ["python", "modeloScoring.py"]
