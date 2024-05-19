import numpy as np
import pandas as pd
import argparse

def preprocesamiento2(input_path: str, output_path: str):
    # Leer el DataFrame de entrada
    df = pd.read_csv(input_path)

    # Añadir columnas NotaConsumidor, Temporada, Estacion
    df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))
    df['Temporada'] = np.random.randint(0, 2, size=len(df))
    df['Estacion'] = np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], size=len(df))

    # Guardar el DataFrame procesado
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocesamiento 2 de datos')
    parser.add_argument('--input_path', type=str, required=True, help='Ruta del archivo CSV de entrada')
    parser.add_argument('--output_path', type=str, required=True, help='Ruta del archivo CSV de salida')
    args = parser.parse_args()
    preprocesamiento2(args.input_path, args.output_path)
