import streamlit as st

import numpy as np

# Crear datos
x = np.linspace(0, 1000, 1000000)
y = np.sin(x)

# Configuración de la aplicación
st.title("Gráfico Interactivo con Streamlit")


