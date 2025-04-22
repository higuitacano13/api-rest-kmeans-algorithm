# 🧠 API REST - K-Means Clustering

**API RESTful desarrollada con FastAPI que permite cargar archivos CSV, procesarlos mediante el algoritmo de clustering no supervisado K-Means y retornar los resultados en formato JSON.** Utiliza la librería Pandas para la manipulación de datos y scikit-learn para la implementación del algoritmo de clustering.

# 🚀 Tecnologías utilizadas
- **FastAPI:** Framework web moderno y de alto rendimiento para construir APIs con Python.
- **Pandas:** Librería para la manipulación y análisis de datos.
- **scikit-learn:** Biblioteca de aprendizaje automático que proporciona herramientas eficientes para análisis predictivo.
- **Uvicorn:** Servidor ASGI ultrarrápido para ejecutar aplicaciones FastAPI.

# ⚙️ Funcionalidades
**1. Carga de archivos CSV**
  - Permite al usuario subir un archivo CSV a través de una solicitud HTTP.
  - El archivo se procesa en memoria sin necesidad de almacenarlo en el servidor.
  
**2. Procesamiento con K-Means** 
  - Aplica el algoritmo de clustering K-Means a los datos proporcionados.
  - El número de clusters (K) puede ser especificado por el usuario o determinado automáticamente utilizando el método del codo.
    
**3. Retorno de resultados**
  - Devuelve los datos originales junto con la asignación de cada punto de datos a un cluster específico.
  - Los resultados se presentan en formato JSON para facilitar su consumo por otras aplicaciones o servicios.

# ✅ Requisitos del entorno
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
