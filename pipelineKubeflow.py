import kfp
from kfp import dsl
from python_scripts.preprocesamiento1 import preprocesamiento1
from python_scripts.preprocesamiento2 import preprocesamiento2
from python_scripts.modeloScoring import modeloScoring


# Definir el pipeline principal
@dsl.pipeline(
    name='Predictor de calidad de plátanos',
    description='Predice si la calidad de los plátanos son buenos o malos con un modelo de XGBoost'
)
def xgb_train_pipeline_local():
    df = "hay que definirlo!!"
    # Componente 1: Pre procesamiento 1
    df_pre1 = preprocesamiento1(df)

    # Componente 2: Pre Procesamiento 2
    df_pre2 = preprocesamiento2(df_pre1)

    # Componente 3: ModeloScoring
    modeloScoring(df_pre2, mes="Marzo")


# Compila y ejecuta el pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(xgb_train_pipeline_local, 'xgb_train_pipeline_local.tar.gz')
