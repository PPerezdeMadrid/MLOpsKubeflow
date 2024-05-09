import h2o
from h2o.estimators import H2OXGBoostEstimator
import pandas as pd
from kfp import dsl, components as comp

def modeloScoring(df: pd.DataFrame, mes: int) -> pd.DataFrame:
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

    # Devolver el DataFrame de predicciones
    return pred_df

modeloscoring_component = comp.func_to_container_op(modeloScoring, packages_to_install=['pandas', 'h2o'])