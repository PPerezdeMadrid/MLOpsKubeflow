# Usa una imagen base que contenga Python
FROM python:3.11

# Instala las dependencias necesarias
RUN pip install numpy

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el script de preprocesamiento2.py al contenedor
COPY preprocesamiento2.py .

# Indica que el contenedor ejecutará este script cuando se inicie
CMD ["python", "preprocesamiento2.py"]
