import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Crear datos
x = np.linspace(0, 1000, 1000000)
y = np.sin(x)

# Configuración de la aplicación
st.title("Gráfico Interactivo con Streamlit")

# Mostrar gráfico interactivo
fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)

# Añadir interactividad con un slider
amplitude = st.slider("Amplitud del seno", 0.1, 10.0, 0.1)
y = amplitude * np.sin(x)
ax.clear()
ax.plot(x, y)

# Fijar límites de los ejes después de limpiar la gráfica
ax.set_xlim(0, 100)
ax.set_ylim(-3, 3)

st.pyplot(fig)
