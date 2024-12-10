# Streamlit Suma

Este proyecto es una aplicación web construida con Streamlit que permite a los usuarios realizar sumas de números de manera interactiva.

## Requisitos

- Docker

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/warc0s/escenario_05_streamlit_suma
   cd escenario_05_streamlit_suma
   ```

2. Construye la imagen de Docker:
   ```bash
   docker build -t streamlit-suma .
   ```

3. Ejecuta el contenedor:
   ```bash
   docker run -p 8501:8501 streamlit-suma
   ```

Luego, abre tu navegador y ve a `http://localhost:8501` para interactuar con la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
