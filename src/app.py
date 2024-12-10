import streamlit as st
import pandas as pd
import numpy as np
import math

# Configuración de la página
st.set_page_config(
    page_title="Calculadora Avanzada",
    page_icon="🧮",
    layout="centered"
)

# Estilo personalizado
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        margin-bottom: 10px;
    }
    .main {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Título y descripción
st.title('🧮 Calculadora Avanzada')
st.markdown("""
Esta calculadora te permite realizar diversas operaciones matemáticas.
Selecciona el tipo de cálculo que deseas realizar y los números con los que quieres operar.
""")

# Selector de operación
operacion = st.selectbox(
    'Selecciona la operación',
    ['Operaciones Básicas', 'Funciones Trigonométricas', 'Operaciones Avanzadas']
)

if operacion == 'Operaciones Básicas':
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input('Primer número', value=0.0)
    with col2:
        num2 = st.number_input('Segundo número', value=0.0)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('➕ Sumar'):
            st.success(f'Resultado: {num1 + num2}')
        if st.button('✖️ Multiplicar'):
            st.success(f'Resultado: {num1 * num2}')
    with col2:
        if st.button('➖ Restar'):
            st.success(f'Resultado: {num1 - num2}')
        if st.button('➗ Dividir'):
            if num2 != 0:
                st.success(f'Resultado: {num1 / num2}')
            else:
                st.error('Error: No se puede dividir por cero')

elif operacion == 'Funciones Trigonométricas':
    angulo = st.number_input('Ingrese el ángulo en grados', value=0.0)
    # Convertir a radianes
    rad = math.radians(angulo)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('Seno'):
            st.success(f'sin({angulo}°) = {math.sin(rad):.4f}')
    with col2:
        if st.button('Coseno'):
            st.success(f'cos({angulo}°) = {math.cos(rad):.4f}')
    with col3:
        if st.button('Tangente'):
            if math.cos(rad) != 0:
                st.success(f'tan({angulo}°) = {math.tan(rad):.4f}')
            else:
                st.error('Error: Tangente indefinida')

else:  # Operaciones Avanzadas
    num = st.number_input('Ingrese un número', value=1.0)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Raíz Cuadrada'):
            if num >= 0:
                st.success(f'√{num} = {math.sqrt(num):.4f}')
            else:
                st.error('Error: No se puede calcular la raíz cuadrada de un número negativo')
        if st.button('Logaritmo Natural'):
            if num > 0:
                st.success(f'ln({num}) = {math.log(num):.4f}')
            else:
                st.error('Error: El logaritmo solo está definido para números positivos')
    with col2:
        if st.button('Potencia al Cuadrado'):
            st.success(f'{num}² = {num ** 2:.4f}')
        if st.button('Valor Absoluto'):
            st.success(f'|{num}| = {abs(num)}')

# Pie de página
st.markdown('---')
st.markdown('Desarrollado con ❤️ usando Streamlit')