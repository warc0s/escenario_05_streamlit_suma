# 🧮 Calculadora Avanzada con Streamlit

Una calculadora interactiva y moderna construida con Streamlit que ofrece múltiples operaciones matemáticas.

## 🌐 ¡Pruébala ahora!

La calculadora está disponible en línea en Streamlit Cloud:
**[https://calculadora-avanzada.streamlit.app/](https://calculadora-avanzada.streamlit.app/)**

¡No necesitas instalar nada! Solo haz clic en el enlace y comienza a calcular.

## ✨ Características

- **Operaciones Básicas**
  - Suma ➕
  - Resta ➖
  - Multiplicación ✖️
  - División ➗

- **Funciones Trigonométricas**
  - Seno
  - Coseno
  - Tangente

- **Operaciones Avanzadas**
  - Raíz Cuadrada
  - Logaritmo Natural
  - Potencia al Cuadrado
  - Valor Absoluto

## 🚀 Instalación Local

1. Clona este repositorio:
```bash
git clone https://github.com/warc0s/escenario_05_streamlit_suma
cd escenario_05_streamlit_suma
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 💻 Uso

1. Ejecuta la aplicación:
```bash
streamlit run app.py
```

2. Abre tu navegador web y accede a la URL mostrada (generalmente http://localhost:8501)

3. Selecciona el tipo de operación que deseas realizar:
   - Elige entre Operaciones Básicas, Funciones Trigonométricas u Operaciones Avanzadas
   - Ingresa los números necesarios
   - Haz clic en el botón de la operación deseada
   - ¡Observa el resultado instantáneo!

## 🐳 Uso con Docker

1. Construye la imagen:
```bash
docker build -t calculadora-streamlit .
```

2. Ejecuta el contenedor:
```bash
docker run -p 8501:8501 calculadora-streamlit
```

3. Accede a la aplicación en tu navegador: http://localhost:8501

## 🛠️ Tecnologías Utilizadas

- Python
- Streamlit
- Pandas
- NumPy
- Math

## 📝 Notas

- La aplicación maneja errores comunes como división por cero
- Las funciones trigonométricas trabajan con ángulos en grados para mayor facilidad
- Los resultados se muestran con 4 decimales de precisión