import kfp
from kfp import dsl
from python_scripts.preprocesamiento1 import preprocesamiento1
from python_scripts.preprocesamiento2 import preprocesamiento2
from python_scripts.modeloScoring import modeloScoring

def obtener_datos():
    pass

# Definir el pipeline principal
@dsl.pipeline(
    name='Predictor de calidad de plátanos',
    description='Predice si la calidad de los plátanos son buenos o malos con un modelo de XGBoost'
)

def xgb_train_pipeline_local():
    df = obtener_datos()

    # Componente 1: Pre procesamiento 1
    df_pre1 = preprocesamiento1(df)

    # Componente 2: Pre Procesamiento 2
    df_pre2 = preprocesamiento2(df_pre1)

    # Componente 3: ModeloScoring
    modeloScoring(df_pre2, mes="Marzo")

def start_pipeline():
    kfp.compiler.Compiler().compile(xgb_train_pipeline_local, 'xgb_train_pipeline_local.tar.gz')

# Compila y ejecuta el pipeline
if __name__ == '__main__':
    start_pipeline()
    # Tenemos que ver esto porq vamos a hacer dos pipeline en la presentación

