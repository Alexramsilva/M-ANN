# -*- coding: utf-8 -*-
"""App Matriz ANN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zU1_ruCkR0kD72GbKt3MZGWlIpEDi_L-
"""

import streamlit as st
import numpy as np


st.image("URC.png", caption="LCFI-URC Universidad Rosario Castellanos", width=200)


import streamlit as st
import numpy as np

# Definir la función ReLU
def relu(z):
    return np.maximum(0, z)

# Definir las operaciones neuronales, ahora con tres capas
def forward_pass(X, W1, b1, W2, b2, W3, b3):
    # Cálculo de Z1
    Z1 = np.dot(X, W1) + b1
    # Aplicar ReLU en Z1 para obtener A1
    A1 = relu(Z1)

    # Cálculo de Z2
    Z2 = np.dot(A1, W2) + b2
    # Aplicar ReLU en Z2 para obtener A2
    A2 = relu(Z2)

    # Cálculo de Z3 (salida final)
    Z3 = np.dot(A2, W3) + b3
    Y_hat = Z3  # Z3 es la salida de la red

    return Z1, A1, Z2, A2, Z3

# Configurar la aplicación Streamlit
st.title('Red Neuronal Simple (Tres Capas)')

st.header('Parámetros de Entrada')

# Entradas para la matriz X
st.subheader('Matriz de Entrada X')
x_rows = st.number_input('Número de filas de X', min_value=1, max_value=10, value=3)
x_cols = st.number_input('Número de columnas de X (dimensión de W1)', min_value=1, max_value=10, value=3)
X = np.random.randn(x_rows, x_cols)
st.write('Matriz X:', X)

# Entradas para W1
st.subheader('Matriz de Pesos W1')
w1_rows = x_cols  # W1 debe tener tantas filas como columnas tenga X
w1_cols = st.number_input('Número de columnas de W1 (dimensión de A1)', min_value=1, max_value=10, value=3)
W1 = np.random.randn(w1_rows, w1_cols)
st.write('Matriz W1:', W1)

# Entradas para el vector b1
st.subheader('Vector de sesgo b1')
b1 = np.random.randn(1, w1_cols)
st.write('Vector b1:', b1)

# Entradas para W2
st.subheader('Matriz de Pesos W2')
w2_rows = w1_cols  # W2 debe tener tantas filas como columnas tenga W1 (dimensión de A1)
w2_cols = st.number_input('Número de columnas de W2 (dimensión de A2)', min_value=1, max_value=10, value=3)
W2 = np.random.randn(w2_rows, w2_cols)
st.write('Matriz W2:', W2)

# Entradas para el vector b2
st.subheader('Vector de sesgo b2')
b2 = np.random.randn(1, w2_cols)
st.write('Vector b2:', b2)

# Entradas para W3
st.subheader('Matriz de Pesos W3')
w3_rows = w2_cols  # W3 debe tener tantas filas como columnas tenga A2
w3_cols = st.number_input('Número de columnas de W3 (dimensión de salida, Z3)', min_value=1, max_value=10, value=1)
W3 = np.random.randn(w3_rows, w3_cols)
st.write('Matriz W3:', W3)

# Entradas para el vector b3
st.subheader('Vector de sesgo b3')
b3 = np.random.randn(1, w3_cols)
st.write('Vector b3:', b3)

# Realizar el forward pass y mostrar resultados
if st.button('Calcular'):
    Z1, A1, Z2, A2, Z3 = forward_pass(X, W1, b1, W2, b2, W3, b3)

    st.subheader('Resultados:')
    st.write('Z1:', Z1)
    st.write('A1 (ReLU(Z1)):', A1)
    st.write('Z2:', Z2)
    st.write('A2 (ReLU(Z2)):', A2)
    st.write('Z3 (Salida Final, Y_hat):', Z3)
# Personalización de diseño
st.markdown("""
<style>
    .stApp {
        background-color:  #da3262;
    }
    .css-1d391kg {
        color:  #faf7f8;
    }
</style>
""", unsafe_allow_html=True)


# Insertar el código HTML con estilos personalizados
st.markdown("""
    <div class="container col-sm-5 creditos text-center">
        <p style="margin-top:0;margin-bottom:0;font-size:15px;color: #424040;text-align:center">
            <strong>Colaboración:</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>Asignatura (UCA): Métodos Cuantitativos  LCFI-URC</strong>
        </p>
        <p style="margin-top:0;margin-bottom:0;font-size:12px;color:  #979394 ;text-align:center">
            <strong>Grupo 103 GAM-LCFI-URC</strong>
        </p>
    </div>
""", unsafe_allow_html=True)