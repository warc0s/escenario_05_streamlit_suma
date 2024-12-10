import streamlit as st
import pandas as pd
import numpy as np

# Título de la aplicación
st.title('Calculadora de Suma')

# Entradas numéricas
num1 = st.number_input('Ingrese el primer número')
num2 = st.number_input('Ingrese el segundo número')

# Botón para calcular la suma
if st.button('Calcular Suma'):
    resultado = num1 + num2
    st.write('La suma es:', resultado)
