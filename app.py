import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Título de tu entorno virtual
st.title("Simulador de Movimiento Parabólico 🚀")

# Controles interactivos en la barra lateral
st.sidebar.header("Configuración del Lanzamiento")
v0 = st.sidebar.slider("Velocidad Inicial (m/s)", 1.0, 50.0, 20.0)
angulo = st.sidebar.slider("Ángulo de Tiro (grados)", 10, 90, 45)
g = st.sidebar.slider("Gravedad (m/s²)", 1.0, 25.0, 9.81)

# Cálculos físicos
theta = np.radians(angulo)
t_vuelo = (2 * v0 * np.sin(theta)) / g
t = np.linspace(0, t_vuelo, 100)

x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Crear el gráfico interactivo
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Trayectoria', line=dict(color='red', width=3)))
fig.update_layout(xaxis_title="Distancia (m)", yaxis_title="Altura (m)", yaxis=dict(range=[0, max(y)*1.1]))

# Mostrar la animación/gráfico en la web
st.plotly_chart(fig)

# Mostrar datos clave automáticamente
st.write(f"**Distancia máxima alcanzada:** {max(x):.2f} metros")
st.write(f"**Tiempo total de vuelo:** {t_vuelo:.2f} segundos")
