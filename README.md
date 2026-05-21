# Análisis Exploratorio de Datos (EDA) - Dataset de Vehículos (EE. UU.)

Este proyecto consiste en una aplicación web interactiva desarrollada con **Streamlit**, diseñada para realizar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de anuncios de venta de vehículos en los Estados Unidos. 

La herramienta permite visualizar de forma dinámica las distribuciones y relaciones clave de las variables del mercado automotriz a través de gráficos interactivos de **Plotly**.

---

## Características de la Aplicación

La interfaz cuenta con controles interactivos (botones) que permiten al usuario desplegar los análisis bajo demanda:

* **Distribución del Odómetro:** Un histograma configurado con 50 contenedores (*bins*) que muestra la concentración del kilometraje de los vehículos e identifica sesgos o valores atípicos en los datos.
* **Relación Precio vs. Odómetro:** Un gráfico de dispersión interactivo (*scatter plot*) que ayuda a analizar visualmente la correlación entre el desgaste del vehículo (kilometraje) y su valor en el mercado.

---

## Tecnologías Utilizadas

* **Python**
* **Streamlit** (Para el desarrollo de la interfaz web interactiva)
* **Pandas** (Para la carga y manipulación del dataset)
* **Plotly (Express & Graph Objects)** (Para la creación de gráficos interactivos y dinámicos)

---

## Instalación y Configuración Local

Sigue estos pasos para clonar el repositorio y ejecutar la aplicación en tu entorno local utilizando **Conda**:

1. Clonar el repositorio:
   git clone [https://github.com/carloscarranza2486/project_sprint_7.git](https://github.com/carloscarranza2486/project_sprint_7.git)
   cd project_sprint_7

2. Crear y activar el entorno virtual con Conda:
   conda create --name vehicles_env python=3.10
   conda activate vehicles_env

3. Instalar las dependencias requeridas:
   pip install -r requirements.txt
   (Si aún no creas el archivo requirements.txt, puedes instalar las librerías directamente con: pip install streamlit pandas plotly)

4. Ejecutar la aplicación:
   streamlit run app.py

---

## Estructura del Proyecto

├── notebooks/          # Contiene el Jupyter Notebook con el análisis de prueba (EDA.ipynb)
├── app.py              # Script principal de la aplicación de Streamlit
├── README.md           # Descripción del proyecto
└── requirements.txt    # Lista de dependencias del proyecto

*(Nota: Asegúrate de que el archivo vehicles_us.csv se encuentre en la ruta correcta fuera del directorio, o ajusta la línea de lectura en app.py según tu configuración de entrega).*