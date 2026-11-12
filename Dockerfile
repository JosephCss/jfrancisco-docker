# 1. Imagen base oficial de Python ligera basada en Debian Linux
FROM python:3.12-slim

# 2. Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar la lista de dependencias al contenedor
COPY requirements.txt .

# 4. Instalar las dependencias de Python sin guardar caché para reducir el tamaño
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente de nuestra aplicación
COPY app.py .

# 6. Documentar el puerto que expone el contenedor
EXPOSE 5000

# 7. Comando que se ejecutará al iniciar el contenedor
CMD ["python", "app.py"]	
