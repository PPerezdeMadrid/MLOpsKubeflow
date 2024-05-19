import pandas as pd
import argparse
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocesamiento1(input_path: str, output_path: str):
    df = pd.read_csv(input_path)

    # Escalar características
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df.drop('Quality', axis=1))
    df_transformado = pd.DataFrame(scaled_features, columns=df.columns[:-1])

    # Codificar variable Quality a (1 y 0)
    label_encoder = LabelEncoder()
    df_transformado['Quality_encoded'] = label_encoder.fit_transform(df['Quality'])

    # Eliminar valores NA
    df_transformado = df_transformado.dropna()

    # Eliminar valores atípicos
    q1 = df_transformado.quantile(0.25)
    q3 = df_transformado.quantile(0.75)
    iqr = q3 - q1
    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr
    df_transformado = df_transformado[~((df_transformado < lower_limit) | (df_transformado > upper_limit)).any(axis=1)]

    df_transformado.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocesamiento de datos')
    parser.add_argument('--input_path', type=str, required=True, help='Ruta del archivo CSV de entrada')
    parser.add_argument('--output_path', type=str, required=True, help='Ruta del archivo CSV de salida')
    args = parser.parse_args()
    preprocesamiento1(args.input_path, args.output_path)
