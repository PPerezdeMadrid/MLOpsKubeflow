import kfp
from kfp import dsl
from kfp.components import InputPath, OutputPath
from MLOpsKubeflow.vertexAI.preprocesamiento1.preprocesamiento1 import preprocesamiento_component
from MLOpsKubeflow.vertexAI.preprocesamiento2.preprocesamiento2 import preprocesamiento2_component
from modeloscoring import modeloscoring_component
from kfp.gcp import components as gcp_components

input_bucket = 'gs://kubeflow-bucket-prueba'
input_csv_file = 'archivo_inputs.csv'

"""
Problemillas que veo:
- como inciar el pipeline
- Añadir un input de "mes" para modeloScoring.py
- Hay que hacer los dockerfile y añadir la imagen al yaml
"""
@dsl.pipeline(
    name='Preprocesamiento Pipeline',
    description='Pipeline para preprocesar datos'
)
def pipeline_completo(
        input_csv: InputPath('CSV'),
        output_csv: OutputPath('CSV')
):
    # Leer el CSV de entrada
    read_csv_op = gcp_components.load_file(
        input_path=input_csv,
        name='Leer CSV de entrada'
    )

    # Ejecutar el componente de preprocesamiento 1
    preprocesamiento_op = preprocesamiento_component(read_csv_op.output)

    # Ejecutar el segundo componente de preprocesamiento
    preprocesamiento2_op = preprocesamiento2_component(preprocesamiento_op.output)

    # Ejecutar el componente de scoring de modelos
    scoring_op = modeloscoring_component(preprocesamiento2_op.output)

    # Convertir el DataFrame de predicciones a CSV y guardarlo en GCS
    save_csv_op = gcp_components.write_to_gcs(
        input_data=scoring_op.output,
        output_path=output_csv,
        name='Guardar CSV de salida'
    )

    # Definir dependencias entre operaciones
    save_csv_op.after(preprocesamiento_op)


# Crear una instancia del cliente de KFP para interactuar con el Kubeflow Pipelines en GCP
client = kfp.Client()

# Compilar y ejecutar el pipeline en Kubeflow Pipelines en GCP
client.create_run_from_pipeline_func(
    pipeline_completo,
    arguments={
        'input_csv': input_bucket + '/' + input_csv_file,
        'output_csv': 'gs://kubeflow-bucket-prueba/scoring.csv'
    }
)