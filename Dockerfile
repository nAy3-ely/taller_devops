# Dockerfile

# 1. Imagen base oficial de Python (versión ligera)
FROM python:3.10-slim

# 2. Etiqueta para identificar al mantenedor
LABEL maintainer="Nayhely Valle"

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# --- PASOS DE INSTALACIÓN DE DEPENDENCIAS ---
# 4. Copiamos el archivo de dependencias (ahora con Flask)
COPY requirements.txt .

# 5. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# --- PASOS DE COPIA DE LA APLICACIÓN ---
# 6. Copiamos los archivos de la aplicación
COPY nayhely.py .

# 7. Comando por defecto al ejecutar el contenedor
# Ejecutamos el script de Python que inicia Flask
CMD ["python", "nayhely.py"]