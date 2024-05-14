# Usar la imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación al directorio de trabajo
COPY . .

# Ejecutar la aplicación
CMD ["python", "modeloScoring.py"]
