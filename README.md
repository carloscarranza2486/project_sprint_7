# # Análisis Exploratorio de Datos (EDA) - Dataset de Vehículos (EE. UU.)

Este proyecto consiste en una aplicación web interactiva desarrollada con **Streamlit**, diseñada para realizar un Análisis Exploratorio de Datos (EDA) sobre un conjunto de datos de anuncios de venta de vehículos en los Estados Unidos. 

La herramienta permite visualizar de forma dinámica las distribuciones y relaciones clave de las variables del mercado automotriz a través de gráficos interactivos de **Plotly**.

---

## Características de la Aplicación

La interfaz cuenta con controles interactivos (botones) que permiten al usuario desplegar los análisis bajo demanda:

* **Distribución del Odómetro:** Un histograma configurado con 50 contenedores (*bins*) que muestra la concentración del kilometraje de los vehículos e identifica sesgos o valores atípicos en los datos.
* **Relación Precio vs. Odómetro:** Un gráfico de dispersión interactivo (*scatter plot*) que ayuda a analizar visualmente la correlación entre el desgaste del vehículo (kilometraje) y su valor en el mercado.

---

## Tech stack

* **Python 3.14+**
* **Streamlit** (Para el desarrollo de la interfaz web interactiva)
* **Pandas** (Para la carga y manipulación del dataset)
* **Plotly (Express & Graph Objects)** (Para la creación de gráficos interactivos y dinámicos)

---

## Instalación y Configuración Local

Sigue estos pasos para clonar el repositorio y ejecutar la aplicación en tu entorno local utilizando **Conda**:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/carloscarranza2486/project_sprint_7.git](https://github.com/carloscarranza2486/project_sprint_7.git)
   cd project_sprint_7