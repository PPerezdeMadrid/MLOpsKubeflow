
## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Archivos de Componentes (Python)**:
  - `preprocesamiento1.py`: Contiene la función de preprocesamiento 1 que escala características, codifica variables y elimina valores atípicos.
  - `preprocesamiento2.py`: Contiene la función de preprocesamiento 2 que añade columnas adicionales al DataFrame.
  - `modeloscoring.py`: Contiene la función que entrena un modelo de machine learning y realiza predicciones.

- **Archivos YAML de Componentes**:
  - `preprocesamiento1.yaml`: Especifica el componente de preprocesamiento 1 como un archivo YAML para Kubeflow Pipeline.
  - `preprocesamiento2.yaml`: Especifica el componente de preprocesamiento 2 como un archivo YAML para Kubeflow Pipeline.
  - `modeloscoring.yaml`: Especifica el componente de modelo de scoring como un archivo YAML para Kubeflow Pipeline.

- **Pipeline Completo**:
  - `pipeline.py`: Contiene la definición del pipeline completo que utiliza los componentes anteriores y establece la lógica de ejecución.

## Contenido de cada Archivo

- **preprocesamiento1.py**:
  - Función que escala características, codifica variables y elimina valores atípicos de un DataFrame.

- **preprocesamiento1.yaml**:
  - Especifica el componente de preprocesamiento 1 como un archivo YAML para Kubeflow Pipeline, incluyendo entradas, salidas e implementación.

- **preprocesamiento2.py**:
  - Función que añade columnas adicionales al DataFrame.

- **preprocesamiento2.yaml**:
  - Especifica el componente de preprocesamiento 2 como un archivo YAML para Kubeflow Pipeline, incluyendo entradas, salidas e implementación.

- **modeloscoring.py**:
  - Función que entrena un modelo de machine learning y realiza predicciones.

- **modeloscoring.yaml**:
  - Especifica el componente de modelo de scoring como un archivo YAML para Kubeflow Pipeline, incluyendo entradas, salidas e implementación.

- **pipeline.py**:
  - Define el pipeline completo que utiliza los componentes anteriores y establece la lógica de ejecución.

## Resumen del Pipeline

El pipeline completo consta de tres etapas:

1. **Preprocesamiento 1**: Escala características, codifica variables y elimina valores atípicos.
2. **Preprocesamiento 2**: Añade columnas adicionales al DataFrame.
3. **Modelo Scoring**: Entrena un modelo de machine learning y realiza predicciones.

Cada etapa del pipeline utiliza un componente específico definido en un archivo YAML, el cual establece las entradas, salidas e implementación del componente.

Este esquema modular permite una fácil reutilización y mantenimiento de cada componente, así como la flexibilidad para construir y modificar el pipeline según sea necesario.