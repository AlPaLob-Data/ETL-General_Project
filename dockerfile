# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias desde requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# Expon el puerto si es necesario (por ejemplo, para una aplicación web)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]