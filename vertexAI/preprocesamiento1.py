from typing import NamedTuple
#import kfp.components as comp
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from kfp.v2.dsl import component

@component(
    base_image="python:3.10", 
    #packages_to_install=['pandas', 'sklearn']
)
def preprocesamiento1(df: pd.DataFrame) -> pd.DataFrame:
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

    return df_transformado

# preprocesamiento_component = comp.func_to_container_op(preprocesamiento1, packages_to_install=['pandas', 'sklearn'])
