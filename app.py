import streamlit as st
from PIL import Image
import os
import time

# --------------------------
# Configuración de la página
# --------------------------
st.set_page_config(page_title="Ramo Digital", page_icon="💛", layout="centered")

# --------------------------
# Fondo bonito usando CSS
# --------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #fffacd, #fff8dc); /* Degradado amarillo suave */
        color: #333333;
    }
    .stButton>button {
        background-color: #ffd700;
        color: #000000;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Mensajes iniciales
# --------------------------
st.markdown("## 💛 Lamento no poder darte las flores de manera física…")
time.sleep(2)
st.markdown("### Pero a pesar de todo, deseo poder tenerte como amiga para toda la vida, Day!")

st.markdown("---")  # Línea separadora

# --------------------------
# Configuración de imágenes
# --------------------------
image_folder = os.path.join(os.getcwd(), "images")  # Carpeta relativa a app.py
image_files = ["flor1.jpg", "foto1.jpg", "foto2.jpg", "foto3.jpg"]  # Cambia según tus imágenes

# Verifica si existen las imágenes
for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    if not os.path.exists(img_path):
        st.warning(f"No se encontró la imagen: {img_file}")

# --------------------------
# Carrusel de imágenes
# --------------------------
st.markdown("### 🌼 Ramo Digital 🌼")

# Crear un "contenedor" donde se van a mostrar las imágenes
image_container = st.empty()

# Mostrar imágenes en loop
while True:
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        if os.path.exists(img_path):
            img = Image.open(img_path)
            image_container.image(img, caption=img_file, use_column_width=True)
            time.sleep(1.5)  # Espera 1.5 segundos antes de la siguiente imagen
