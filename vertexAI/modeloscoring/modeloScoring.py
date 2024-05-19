import h2o
from h2o.estimators import H2OXGBoostEstimator
import pandas as pd
from kfp import dsl, components 

@component(
    base_image="imagen_modelo_scoring:latest", # package to install
)

def modeloScoring(input_csv_path: str, mes: int, ruta_bucket_csv: str):
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Modelo de Scoring')
    parser.add_argument('--input_csv_path', type=str, required=True, help='Ruta del archivo CSV de entrada')
    parser.add_argument('--mes', type=int, required=True, help='Mes de los datos')
    parser.add_argument('--ruta_bucket_csv', type=str, required=True, help='Ruta del bucket para guardar el archivo CSV de salida')
    args = parser.parse_args()
    modeloScoring(args.input_csv_path, args.mes, args.ruta_bucket_csv)