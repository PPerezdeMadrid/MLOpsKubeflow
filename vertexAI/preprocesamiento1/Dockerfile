# Usa una imagen de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el código actual al contenedor en /app
COPY preprocesamiento1.py .

# Instala las dependencias de Python
RUN pip install --no-cache-dir pandas scikit-learn kfp

# Define el comando por defecto para ejecutar tu aplicación
CMD ["python", "preprocesamiento1.py"]
