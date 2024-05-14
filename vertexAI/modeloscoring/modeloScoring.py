import h2o
from h2o.estimators import H2OXGBoostEstimator
import pandas as pd
from kfp import dsl, components 

@component(
    base_image="imagen_modelo_scoring:latest", # package to install
)

def modeloScoring(df: pd.DataFrame, mes: int, ruta_bucket_csv: str) -> pd.DataFrame:
    df_mes = df[df['Mes'] == mes].copy()
    
    h2o.init()
    data = h2o.H2OFrame(df_mes)

    # Creacion de subconjuntos
    predictors = ["Precio", "NotaConsumidor", "Size", "Weight", "Sweetness", "Softness", "HarvestTime", "Ripeness", "Acidity"]
    response = "Quality_encoded"

    data[response] = data[response].asfactor()

    # Dividir los datos en train + dev + test
    train, test, dev = data.split_frame(ratios=[0.75, 0.15], destination_frames=['train_df', 'test_df', 'val_df'], seed=566)

    # Entrenar el modelo
    xgb = H2OXGBoostEstimator()
    xgb.train(x=predictors, y=response, training_frame=train, validation_frame=dev)

    # Hacer predicciones y evaluar el modelo
    pred = xgb.predict(test)
    evaluacion = xgb.model_performance(test)

    # Obtener las predicciones como un DataFrame de Pandas
    pred_df = pred.as_data_frame()
    
    # Guardarlo en el bucket 
    fecha_actual = pd.Timestamp.now().strftime('%Y-%m-%d')
    nombre_archivo_csv = f"scoring_{fecha_actual}.csv"
    ruta_completa = f"{ruta_bucket_csv}/{nombre_archivo_csv}"
    pred_df.to_csv(ruta_completa, index=False)

# modeloscoring_component = comp.func_to_container_op(modeloScoring, packages_to_install=['pandas', 'h2o'])