import numpy as np
from typing import NamedTuple
import kfp
from kfp import dsl, components as comp

def preprocesamiento2(df):
    # Añadimos una columna Nota, Temporada, Estacion
    df['NotaConsumidor'] = np.random.randint(0, 11, size=len(df))
    df['Temporada'] = np.random.randint(0, 2, size=len(df))
    df['Estacion'] = np.random.choice(['Primavera', 'Verano', 'Otoño', 'Invierno'], size=len(df))
    return df

preprocesamiento2_component = comp.func_to_container_op(preprocesamiento2, packages_to_install=['numpy'])