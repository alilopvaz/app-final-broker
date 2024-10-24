import streamlit as st
import base64
import pandas as pd
import numpy as np

# Cargar el logo
logo_path = r'logo1.png'
with open(logo_path, "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode('utf-8')

# Cargar el logo de UiPath
imagen_uipath = r'uipath.png'
with open(imagen_uipath, "rb") as image_file:
    encoded_imagen_uipath = base64.b64encode(image_file.read()).decode('utf-8')

# Incluir Bootstrap CSS para el estilo si es necesario
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# CSS para modificar el estilo de los botones y las imágenes
st.markdown(f"""
    <style>
    /* Fijar el navbar en la parte superior */
    .stApp header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #F8F9FA;
        z-index: 1000;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 20px;
    }}

    /* Estilo del logo */
    .stApp header .navbar-brand {{
        display: flex;
        align-items: center;
        width: 3%;
        height: 3%;
    }}
    
    .stApp header img {{
        width: 60px;
        height: 40px;
    }}

    /* Estilos personalizados para los botones del navbar */
    .stButton>button {{
        background-color: #F8F9FA;
        color: black; /* Color del texto */
        border: none; /* Sin borde */
        padding: 10px 20px; /* Espaciado interno */
        font-size: 16px; /* Tamaño de fuente */
        margin: 10px; /* Márgenes alrededor */
        cursor: pointer; /* Cambiar el cursor al pasar por encima */
        border-radius: 5px; /* Bordes redondeados */
        position: fixed; /* Fijar la posición */
        top: 0; /* Arriba del todo */
        z-index: 1001; /* Asegurar que estén por encima de otros elementos */
        justify-content: flex-end;
    }}

    /* Estilo para el hover de los botones */
    .stButton>button:hover {{
        background-color: #9DC0DA; /* Color al pasar el mouse */
        color: white;
    }}

    /* Alinear y centrar verticalmente la imagen de UiPath */
    .navbar-logo-right {{
        display: flex;
        align-items: center; /* Centrar verticalmente */
        position: absolute;
        right: 20px;
        top: 0;
        height: 100%; /* Asegurarse de que ocupa toda la altura del navbar */
    }}

    .navbar-logo-right img {{
        width: 10%;
        height: 10%;
    }}
    </style>
""", unsafe_allow_html=True)

# Crear el header con el logo y el logo de UiPath alineado a la derecha
st.markdown(f"""
    <header class="navbar">
        <div class="navbar-brand">
            <img src="data:image/png;base64,{encoded_logo}" alt="Logo">
        </div>
        <div class="navbar-logo-right">
            <img src="data:image/png;base64,{encoded_imagen_uipath}" alt="UiPath Logo">
        </div>
    </header>
""", unsafe_allow_html=True)

# Inicialización de sesión para manejar la navegación entre secciones
if 'selected_section' not in st.session_state:
    st.session_state['selected_section'] = 'home'  # Sección por defecto

# Crear los botones del navbar (los botones reales de Streamlit)
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Home"):
        st.session_state['selected_section'] = 'home'

with col2:
    if st.button("Processes"):
        st.session_state['selected_section'] = 'processes'

with col3:
    if st.button("Jobs"):
        st.session_state['selected_section'] = 'jobs'

with col4:
    if st.button("Machines"):
        st.session_state['selected_section'] = 'machines'

with col5:
    if st.button("Planning"):
        st.session_state['selected_section'] = 'planning'

# Mostrar contenido según la sección seleccionada
if st.session_state['selected_section'] == 'home':
    st.write("## Home Section")
    st.write("Welcome to the Home section.")

elif st.session_state['selected_section'] == 'processes':
    st.write("## Processes Section")
    st.write("Details about the process go here.")

elif st.session_state['selected_section'] == 'jobs':
    st.write("## Jobs Section")

    # Crear una tabla con las columnas específicas
    columns = [
        "robot", "dateInsert", "dateUpdate", "state", "jobId", "processVer",
        "machineName", "windowsId", "robotName", "jobSLcode", "jobSLMessage"
    ]

    # Generar datos de ejemplo
    data = {
        "robot": [f"Robot-{i}" for i in range(1, 51)],  # 50 robots
        "dateInsert": pd.date_range(start="2023-01-01", periods=50, freq="D"),
        "dateUpdate": pd.date_range(start="2023-02-01", periods=50, freq="D"),
        "state": np.random.choice(["Running", "Stopped", "Idle"], size=50),
        "jobId": [f"Job-{i}" for i in range(1, 51)],
        "processVer": np.random.randint(1, 5, size=50),
        "machineName": [f"Machine-{i}" for i in range(1, 51)],
        "windowsId": [f"Win-{i}" for i in range(1, 51)],
        "robotName": [f"RobotName-{i}" for i in range(1, 51)],
        "jobSLcode": np.random.randint(1000, 9999, size=50),
        "jobSLMessage": [f"Message-{i}" for i in range(1, 51)],
    }

    # Convertir los datos en un DataFrame de Pandas
    df = pd.DataFrame(data)

    # Definir el número de filas por página
    rows_per_page = 10
    total_pages = (len(df) - 1) // rows_per_page + 1

    # Slider para seleccionar la página
    page = st.slider("Página", 1, total_pages, 1)

    # Calcular los índices de los datos para la página seleccionada
    start_idx = (page - 1) * rows_per_page
    end_idx = start_idx + rows_per_page

    # Mostrar la tabla
    st.table(df.iloc[start_idx:end_idx])

elif st.session_state['selected_section'] == 'machines':
    st.write("## Machines Section")
    st.write("Information about machines goes here.")

elif st.session_state['selected_section'] == 'planning':
    st.write("## Planning Section")
    st.write("Details about planning go here.")
